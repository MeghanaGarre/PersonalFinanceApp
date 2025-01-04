import unittest
from db.database import init_db, save_user, get_user_by_username, add_transaction, view_transactions

class TestPersonalFinanceApp(unittest.TestCase):

    def setUp(self):
        init_db()
        save_user("testuser", "testpassword")

    def test_user_registration(self):
        user = get_user_by_username("testuser")
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "testuser")

    def test_add_transaction(self):
        add_transaction("testuser", 100.0, "Salary", "income")
        transactions = view_transactions("testuser")
        self.assertGreater(len(transactions), 0)
        self.assertEqual(transactions[0][1], "testuser")
        self.assertEqual(transactions[0][2], 100.0)

if __name__ == "__main__":
    unittest.main()
