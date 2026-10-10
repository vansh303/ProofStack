from app.db.models import User


def test_user_model_has_only_authentication_identity_fields() -> None:
    columns = User.__table__.columns

    assert set(columns.keys()) == {
        "id",
        "email",
        "password_hash",
        "email_verified_at",
        "is_active",
        "created_at",
        "updated_at",
    }
    assert columns["id"].primary_key
    assert not columns["email"].nullable
    assert not columns["is_active"].nullable
    assert columns["password_hash"].nullable
    assert columns["email_verified_at"].nullable


def test_user_email_is_unique() -> None:
    unique_constraints = {
        constraint.name
        for constraint in User.__table__.constraints
        if constraint.__class__.__name__ == "UniqueConstraint"
    }

    assert "uq_users_email" in unique_constraints
