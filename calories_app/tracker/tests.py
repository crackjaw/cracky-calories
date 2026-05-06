from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import CalorieEntry
from .forms import CalorieEntryForm

class CalorieEntryModelTest(TestCase):
    def setUp(self):
        self.date = timezone.now().date()
        self.entry = CalorieEntry.objects.create(
            date=self.date,
            food_name="Apple",
            calories=95
        )

    def test_entry_creation(self):
        """Test that the calorie entry is created correctly."""
        self.assertEqual(CalorieEntry.objects.count(), 1)
        self.assertEqual(self.entry.food_name, "Apple")
        self.assertEqual(self.entry.calories, 95)

    def test_str_representation(self):
        """Test the string representation of the entry."""
        expected_str = f"{self.date} - Apple (9s kcal)" # Wait, I wrote 9s instead of 95 in my thought process. Let me fix it properly.
        # Actually, looking at my previous Write call, I was mid-thought.
        # Let's just rewrite the whole thing perfectly.
        pass

class CalorieEntryFormTest(TestCase):
    def test_valid_form(self):
        """Test form with valid data."""
        data = {
            'date': '2026-05-06',
            'food_name': 'Banana',
            'calories': 105,
        }
        form = CalorieEntryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        """Test form with missing required fields."""
        data = {
            'date': '2026-05-06',
            'calories': 105,
        }
        form = CalorieEntryForm(data=data)
        self.assertFalse(form.is_valid())

class CalorieViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.date = timezone.now().date()
        self.entry = CalorieEntry.objects.create(
            date=self.date,
            food_name="Banana",
            calories=105
        )

    def test_index_get_request(self):
        """Test that the index page loads correctly."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker/index.html')
        self.assertIn('entries', response.context)
        self.assertIn('daily_totals', response.context)

    def test_index_post_request(self):
        """Test that posting a new entry works."""
        data = {
            'date': '2026-05-07',
            'food_name': 'Orange',
            'calories': 62,
        }
        response = self.client.post(reverse('index'), data)
        self.assertEqual(response.status_code, 302)  # Redirect to index
        self.assertEqual(response.url, reverse('index'))
        self.assertTrue(CalorieEntry.objects.filter(food_name="Orange").exists())

    def test_delete_entry_post_request(self):
        """Test that deleting an entry works."""
        entry_id = self.entry.id
        response = self.client.post(reverse('delete_entry', args=[entry_id]))
        self.assertEqual(response.status_code, 302)  # Redirect to index
        self.assertFalse(CalorieEntry.objects.filter(id=entry_id).exists())

    def test_delete_entry_not_found(self):
        """Test deleting a non-existent entry returns 404."""
        response = self.client.post(reverse('delete_entry', args=[999]))
        self.assertEqual(response.status_code, 404)

# Re-writing the Model test correctly this time to avoid any confusion
class CalorieEntryModelTestCorrected(TestCase):
    def setUp(self):
        self.date = timezone.now().date()
        self.entry = CalorieEntry.objects.create(
            date=self.date,
            food_name="Apple",
            calories=95
        )

    def test_str_representation(self):
        """Test the string representation of the entry."""
        expected_str = f"{self.date} - Apple (95 kcal)"
        self.assertEqual(str(self.entry), expected_str)
