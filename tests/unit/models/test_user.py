"""
Contains tests for app.models.User class
"""
# pylint: disable=redefined-outer-name,unused-argument
# from unittest import mock
import pytest
from app.models import User, Post
from app import db
from datetime import datetime, timedelta

@pytest.fixture
def user1():
    """
    User object
    """
    return User(
        username='john',
        email='john@example.com',
        about_me="Hello",
    )


def test_new_user(user1):
    """
    Test that user object contain correct values
    """
    assert user1.email == 'john@example.com'
    assert user1.username == "john"
    assert user1.about_me == 'Hello'
    assert str(user1) == "<User john, john@example.com>"

def test_password_hashing(test_app, user1):
    """
    Test setting password for user
    """
    user1.set_password('cat')
    assert user1.check_password('dog') is False
    assert user1.check_password('cat') is True

def test_avatar(test_app, user1):
    """
    Test creation of Gravatar URL
    """
    assert user1.avatar(128) == ('https://www.gravatar.com/avatar/'
                                 'd4c74594d841139328695756648b6bd6'
                                 '?d=retro&s=128')

def test_follow(test_app):
    """
    Test that follow appends a followed user to followed
    Test that unfollow removes the user to followed.
    """
    user1 = User(username='john', email='john@example.com')
    user2 = User(username='jane', email='jane@example.com')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    assert user1.followed.all () == []

    user1.follow(user2)
    db.session.commit()
    assert user1.is_following(user2) is True
    assert user1.followed.count() == 1
    assert user1.followed.first().username == 'jane'
    assert user2.followers.count() == 1
    assert user2.followers.first().username == 'john'

    user1.unfollow(user2)
    db.session.commit()
    assert user1.is_following(user2) is not True
    assert user1.followed.count() == 0
    assert user2.followers.count() == 0

def test_follow_posts(test_app):
    """
    Test that followed posts are returned correctly.
    """
    user1 = User(username='john', email='john@example.com')
    user2 = User(username='jane', email='jane@example.com')
    user3 = User(username='susan', email='susan@example.com')
    user4 = User(username='mike', email='mike@example.com')
    db.session.add_all([user1, user2, user3, user4])

    now = datetime.utcnow()
    p1 = Post(body="post from john", author=user1,
              timestamp=now + timedelta(seconds=1))
    p2 = Post(body="post from jane", author=user2,
              timestamp=now + timedelta(seconds=4))
    p3 = Post(body="post from susan", author=user3,
              timestamp=now + timedelta(seconds=3))
    p4 = Post(body="post from mike", author=user4,
              timestamp=now + timedelta(seconds=2))
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()

    user1.follow(user2)  # john follows jane
    user1.follow(user4)  # john follows mike
    user2.follow(user3)  # jane follows susan
    user3.follow(user4)  # susan follows mike
    db.session.commit()

    follow1 = user1.followed_posts().all()
    follow2 = user2.followed_posts().all()
    follow3 = user3.followed_posts().all()
    follow4 = user4.followed_posts().all()

    assert follow1 == [p2, p4, p1]
    assert follow2 == [p2, p3]
    assert follow3 == [p3, p4]
    assert follow4 == [p4]