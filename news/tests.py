import datetime as dt
from django.test import TestCase
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
        

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2024-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

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
