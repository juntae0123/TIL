from django.urls import reverse
from django.test import TestCase

from .models import Post


class AssetBoardTests(TestCase):
    def setUp(self):
        Post.objects.create(asset_id="stock-kospi", title="첫 글", content="내용1", author="테스터")
        Post.objects.create(asset_id="stock-kospi", title="두번째 글", content="내용2", author="익명")
        Post.objects.create(asset_id="bitcoin", title="다른 자산 글", content="내용3", author="테스터")

    def test_asset_list_uses_json_data(self):
        response = self.client.get(reverse("assets:asset_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "KOSPI 주식")
        self.assertContains(response, "금")
        self.assertContains(response, "게시글 수:")

    def test_asset_detail_displays_asset_info(self):
        response = self.client.get(reverse("assets:asset_detail", args=["stock-kospi"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "KOSPI 주식")
        self.assertContains(response, "카테고리:")
        self.assertContains(response, "첫 글")
        self.assertContains(response, "두번째 글")
        self.assertNotContains(response, "다른 자산 글")

    def test_post_form_blocks_forbidden_content(self):
        response = self.client.post(
            reverse("assets:post_create", args=["stock-kospi"]),
            {
                "title": "욕설입니다",
                "content": "이 내용은 혐오적입니다.",
                "author": "테스터",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "부적절한 내용이 포함되어 있습니다. 수정 후 다시 등록해 주세요.")

    def test_post_delete_removes_post_and_redirects(self):
        post = Post.objects.create(asset_id="stock-kospi", title="삭제 테스트", content="삭제할 글", author="테스터")
        response = self.client.post(reverse("assets:post_delete", args=["stock-kospi", post.pk]))
        self.assertRedirects(response, reverse("assets:asset_detail", args=["stock-kospi"]))
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())
