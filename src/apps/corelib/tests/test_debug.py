import pytest
from django.db import connections
from django.db.utils import OperationalError


@pytest.mark.django_db
def test_database_connection():
    """
    Test that the database connection is working.
    """
    db_conn = connections["default"]
    try:
        cursor = db_conn.cursor()
    except OperationalError:
        pytest.fail("Database connection failed")
