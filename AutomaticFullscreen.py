import sublime
import sublime_plugin


def plugin_loaded():
    for window in sublime.windows():
        window.run_command("toggle_full_screen")
