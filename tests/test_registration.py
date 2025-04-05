import pytest
import sqlite3
import os
from registration.registration import create_db, add_user, authenticate_user, display_users

def test_add_existing_user(setup_database):
    """Тест добавления пользователя с существующим логином."""
    add_user('duplicateuser', 'dup@example.com', 'pass123')
    result = add_user('duplicateuser', 'other@example.com', 'pass456')
    assert result is False or result is None, "Добавление пользователя с существующим логином должно быть запрещено."


def test_successful_authentication(setup_database):
    """Тест успешной аутентификации пользователя."""
    add_user('authuser', 'auth@example.com', 'secret123')
    assert authenticate_user('authuser', 'secret123'), "Пользователь должен пройти аутентификацию с правильными данными."


def test_authentication_wrong_password(setup_database):
    """Тест аутентификации с неправильным паролем."""
    add_user('wrongpassuser', 'wp@example.com', 'rightpass')
    assert not authenticate_user('wrongpassuser', 'wrongpass'), "Аутентификация с неправильным паролем должна провалиться."


def test_authentication_nonexistent_user(setup_database):
    """Тест аутентификации несуществующего пользователя."""
    assert not authenticate_user('ghostuser', 'any'), "Невозможно аутентифицировать несуществующего пользователя."


def test_display_users_output(capfd, setup_database):
    """Тест отображения списка пользователей (проверка вывода в консоль)."""
    add_user('user1', 'u1@example.com', 'pass1')
    add_user('user2', 'u2@example.com', 'pass2')
    display_users()
    out, _ = capfd.readouterr()
    assert 'user1' in out and 'user2' in out, "Ожидается вывод добавленных пользователей." 'testuser@example.com', 'password123')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username='testuser';")
    user = cursor.fetchone()
    assert user, "Пользователь должен быть добавлен в базу данных."

