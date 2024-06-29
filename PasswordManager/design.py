import os
import shutil


def print_center(text):
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    text_length = len(text)

    space_count = (terminal_width-text_length) // 2

    print(" " * space_count + text)

def print_big_text(text):
    big_text = f"""
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █▀▄
{text}
    """

    print(big_text)
def clear_console():
    os.system('cls')
    print_big_text("Developed by Deniz Varıcı")

