from model_mommy import mommy

from django.test import TestCase

from redeneural.blog.models import Category, Post


class CategoryModelTestCase(TestCase):

    def setUp(self):
        self.obj = Category(meetup_group=mommy.make('meetup_group.MeetupGroup'), title='Title', slug='slug')
        self.obj.save()

        self.field_title = Category._meta.get_field('title')
        self.field_slug = Category._meta.get_field('slug')

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.title)

    # TITLE
    def test_title_cant_be_blank(self):
        self.assertFalse(self.field_title.blank)

    def test_title_cant_be_null(self):
        self.assertFalse(self.field_title.null)

    # SLUG
    def test_slug_can_be_blank(self):
        self.assertFalse(self.field_slug.blank)

    def test_slug_cant_be_null(self):
        self.assertFalse(self.field_slug.null)


class PostModelTestCase(TestCase):

    def setUp(self):
        self.obj = Post(meetup_group=mommy.make('meetup_group.MeetupGroup'), category=mommy.make(Category),
                        title='Title', slug='title', content='content')
        self.obj.save()

        self.field_meetup_group = Post._meta.get_field('meetup_group')
        self.field_category = Post._meta.get_field('category')
        self.field_title = Post._meta.get_field('title')
        self.field_slug = Post._meta.get_field('slug')
        self.field_content = Post._meta.get_field('content')

    def test_str(self):
        self.assertEqual(str(self.obj), self.obj.title)

    # MEETUP GROUP
    def test_meetup_group_can_be_blank(self):
        self.assertFalse(self.field_meetup_group.blank)

    def test_meetup_group_cant_be_null(self):
        self.assertFalse(self.field_meetup_group.null)

    # CATEGORY
    def test_category_can_be_blank(self):
        self.assertFalse(self.field_category.blank)

    def test_category_cant_be_null(self):
        self.assertFalse(self.field_category.null)

    # TITLE
    def test_title_can_be_blank(self):
        self.assertFalse(self.field_title.blank)

    def test_title_cant_be_null(self):
        self.assertFalse(self.field_title.null)

    # SLUG
    def test_slug_can_be_blank(self):
        self.assertFalse(self.field_slug.blank)

    def test_slug_cant_be_null(self):
        self.assertFalse(self.field_slug.null)

    # CONTENT
    def test_content_can_be_blank(self):
        self.assertFalse(self.field_content.blank)

    def test_content_cant_be_null(self):
        self.assertFalse(self.field_content.null)
