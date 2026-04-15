# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

from pyrogram import filters
from pyrogram.enums import ChatType

# Stores user login steps
user_steps = {}


def login_filter_func(_, __, message):
    """
    Custom filter to check if a user is in login process.
    Safely handles cases where message or from_user is None.
    """

    # Ignore invalid updates (channel posts, anonymous admins, etc.)
    if not message or not message.from_user:
        return False

    # (Optional) Restrict to private chats only
    if message.chat.type != ChatType.PRIVATE:
        return False

    user_id = message.from_user.id

    return user_id in user_steps


# Create Pyrogram filter
login_in_progress = filters.create(login_filter_func)


def set_user_step(user_id, step=None):
    """
    Set or remove a user's login step.
    """
    if step is not None:
        user_steps[user_id] = step
    else:
        user_steps.pop(user_id, None)


def get_user_step(user_id):
    """
    Get current step of a user.
    """
    return user_steps.get(user_id)


def clear_all_steps():
    """
    (Optional) Clear all user steps (useful for reset/debug).
    """
    user_steps.clear()
