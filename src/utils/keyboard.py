from typing import KeysView
from telebot import types
from types import SimpleNamespace
import emoji


def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    """
     Create a keyboard from a list of keys.

     Example:
        keys = ['a', 'b','c']
    """
    markup = types.ReplyKeyboardMarkup(row_width==row_width, resize_keyboard==resize_keyboard)
    keys = map(emoji.emojize, keys)
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)

    return markup