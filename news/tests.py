from django.utils import timezone
from django.test import TestCase, tag
from .models import Editor,Article,tags

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        

class ArticleModelTest(TestCase):
    def setUp(self):
        self.editor = Editor.objects.create(first_name = 'Test', last_name ='Editor', email ='testeditor@moringaschool.com')
        self.tag1 = tags.objects.create(name="Tag1")
        self.tag2 = tags.objects.create(name="Tag2")
        self.article = Article.objects.create(
            title="Test Article",
            post="This is a test article.",
            editor=self.editor,
        )
        self.article.tags.add(self.tag1, self.tag2)

    def test_create_article(self):
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.post, "This is a test article.")
        self.assertEqual(self.article.editor, self.editor)
        self.assertEqual(self.article.tags.count(), 2)
    
    def test_delete_article(self):
        article_id = self.article.id
        self.article.delete()
        self.assertEqual(Article.objects.count(), 0)
        with self.assertRaises(Article.DoesNotExist):
            Article.objects.get(id=article_id)
    
    def test_display_all_articles(self):
        Article.objects.create(
            title="Second Article",
            post="This is another test article.",
            editor=self.editor,
        )
        articles = Article.objects.all()
        self.assertEqual(articles.count(), 2)
        self.assertIn(self.article, articles)

    def test_update_article(self):
        new_title = "Updated Test Article"
        new_post = "This is an updated test article."
        new_editor = Editor.objects.create(first_name = 'New', last_name ='Editor', email ='neweditor@moringaschool.com')
        new_tag = tags.objects.create(name="NewTag")

        self.article.title = new_title
        self.article.post = new_post
        self.article.editor = new_editor
        self.article.tags.add(new_tag)
        self.article.save()

        updated_article = Article.objects.get(id=self.article.id)
        self.assertEqual(updated_article.title, new_title)
        self.assertEqual(updated_article.post, new_post)
        self.assertEqual(updated_article.editor, new_editor)
        self.assertEqual(updated_article.tags.count(), 3)
        self.assertIn(new_tag, updated_article.tags.all())

    def test_article_pub_date(self):
        self.assertIsNotNone(self.article.pub_date)
        self.assertTrue(isinstance(self.article.pub_date, timezone.datetime))
        self.assertLess(self.article.pub_date, timezone.now())

class TagsModelTest(TestCase):
    def setUp(self):
        self.tag1 = tags.objects.create(name="Python")
        self.tag2 = tags.objects.create(name="Django")
        self.tag3 = tags.objects.create(name="Testing")

    def test_delete_tag(self):
        """Test for deleting a model object."""
        initial_count = tags.objects.count()
        self.tag1.delete()
        self.assertEqual(tags.objects.count(), initial_count - 1)
        with self.assertRaises(tags.DoesNotExist):
            tags.objects.get(id=self.tag1.id)

    def test_display_all_tags(self):
        """Test for displaying all model objects saved."""
        all_tags = tags.objects.all()
        self.assertEqual(all_tags.count(), 3)
        self.assertIn(self.tag1, all_tags)
        self.assertIn(self.tag2, all_tags)
        self.assertIn(self.tag3, all_tags)

    def test_update_tag(self):
        """Test for updating single object properties."""
        new_name = "Updated Python"
        self.tag1.name = new_name
        self.tag1.save()
        
        updated_tag = tags.objects.get(id=self.tag1.id)
        self.assertEqual(updated_tag.name, new_name)

    def test_tag_str_method(self):
        """Test the __str__ method of the tags model."""
        self.assertEqual(str(self.tag1), "Python")
        self.assertEqual(str(self.tag2), "Django")
