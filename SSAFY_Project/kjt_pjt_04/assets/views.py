import json
from pathlib import Path

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count

from .forms import PostForm
from .models import Post

ASSETS_JSON_PATH = Path(__file__).resolve().parents[1] / "data" / "assets.json"


def load_assets_data():
    if not ASSETS_JSON_PATH.exists():
        return []
    with ASSETS_JSON_PATH.open(encoding="utf-8") as f:
        return json.load(f)


ASSET_DATA = load_assets_data()


def get_asset_info(asset_id):
    for asset in ASSET_DATA:
        if asset.get("id") == asset_id:
            asset_copy = asset.copy()
            asset_copy["asset_id"] = asset_copy["id"]
            return asset_copy
    return {
        "id": asset_id,
        "asset_id": asset_id,
        "name": f"{asset_id} 자산",
        "category": "알 수 없음",
        "description": f"선택한 자산 {asset_id}에 대한 토론 게시판입니다.",
        "risk_level": "-",
    }


def asset_list(request):
    assets = []
    post_counts = {item["asset_id"]: item["post_count"] for item in Post.objects.values("asset_id").annotate(post_count=Count("id"))}
    for asset in ASSET_DATA:
        asset_copy = asset.copy()
        asset_copy["asset_id"] = asset_copy["id"]
        asset_copy["post_count"] = post_counts.get(asset_copy["asset_id"], 0)
        assets.append(asset_copy)
    return render(request, "assets/asset_list.html", {"assets": assets})


def asset_detail(request, asset_id):
    asset = get_asset_info(asset_id)
    posts = Post.objects.filter(asset_id=asset_id).order_by("-created_at")
    return render(request, "assets/asset_detail.html", {"asset": asset, "posts": posts})


def post_detail(request, asset_id, post_pk):
    asset = get_asset_info(asset_id)
    post = get_object_or_404(Post, pk=post_pk, asset_id=asset_id)
    return render(request, "assets/post_detail.html", {"asset": asset, "post": post})


def post_create(request, asset_id):
    asset = get_asset_info(asset_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.asset_id = asset_id
            post.save()
            return redirect("assets:post_detail", asset_id=asset_id, post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, "assets/post_form.html", {"asset": asset, "form": form})


def post_update(request, asset_id, post_pk):
    asset = get_asset_info(asset_id)
    if asset["category"] == "알 수 없음" and asset["id"] == asset_id:
        raise Http404("존재하지 않는 금융 자산입니다.")

    post = get_object_or_404(Post, pk=post_pk, asset_id=asset_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("assets:post_detail", asset_id=asset_id, post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "assets/post_form.html", {"asset": asset, "form": form, "post": post})


def post_delete(request, asset_id, post_pk):
    post = get_object_or_404(Post, pk=post_pk, asset_id=asset_id)
    if request.method == "POST":
        post.delete()
        return redirect("assets:asset_detail", asset_id=asset_id)
    asset = get_asset_info(asset_id)
    return render(request, "assets/post_detail.html", {"asset": asset, "post": post})

