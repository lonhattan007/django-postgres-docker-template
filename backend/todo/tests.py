from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from todo.views import TodoView

# Create your tests here.


class TodoRequestsTest(APITestCase):
    """Testing todo-related requests to the server"""

    def test_get_request(self):
        request = APIRequestFactory().get("/api/todos/")
        view = TodoView.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todo(self):
        request = APIRequestFactory().post(
            "/api/todos/",
            {
                "title": "New todo item",
                "description": "New todo item description",
                "completed": False,
            },
        )
        view = TodoView.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_bad_request(self):
        request = APIRequestFactory().post(
            "/api/todos/",
            {
                "title": "New todo item with empty description",
                "description": "",
                "completed": False,
            },
        )
        view = TodoView.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
