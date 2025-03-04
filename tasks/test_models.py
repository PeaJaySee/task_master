from django.test import TestCase
from .models import Task, Category

class TaskModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Test Task",
            due_date="2025-03-04",
            complete=False,
            category=self.category
        )

    def test_task_creation(self):
        # Test task creation
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.due_date, "2025-03-04")
        self.assertEqual(self.task.complete, False)
        self.assertEqual(self.task.category, self.category)

    def test_task_str(self):
        # Test the string representation of the task
        self.assertEqual(str(self.task), "Test Task")

    def test_task_due_date(self):
        # Test the due date of the task
        self.assertEqual(self.task.due_date, "2025-03-04")


    def test_task_complete(self):
        # Test the complete status of the task
        self.assertEqual(self.task.complete
, False)
        

    def test_task_category_relationship(self):
        # Test for the relationship between the task and the category
        self.assertEqual(self.task.category, self.category)


#generate a unit test that checks for an error if the title is longer than 100 characters
    def test_task_title_length(self):
        # Test for the length of the title
        with self.assertRaises(ValueError):
            Task.objects.create(
                title="This is a very long title that is over 100 characters long and should raise an error",
                due_date="2025-03-04",
                complete=False,
                category=self.category
            )


