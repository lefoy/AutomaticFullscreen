import sublime
import sublime_plugin


def plugin_loaded():
    sublime.active_window().run_command("toggle_full_screen")
