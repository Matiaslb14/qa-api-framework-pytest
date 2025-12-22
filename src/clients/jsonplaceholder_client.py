from src.clients.base_client import BaseClient


class JsonPlaceholderClient(BaseClient):

    # ---------- USERS ----------
    def get_user(self, user_id: int):
        return self.get(f"/users/{user_id}")

    def get_all_users(self):
        return self.get("/users")

    # ---------- POSTS ----------
    def get_posts(self, params: dict | None = None):
        return self.get("/posts", params=params)

    def get_post(self, post_id: int):
        return self.get(f"/posts/{post_id}")

    def create_post(self, payload: dict):
        return self.post("/posts", json=payload)
