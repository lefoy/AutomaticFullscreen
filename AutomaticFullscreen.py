import sublime
import sublime_plugin


class CurrentPathStatusCommand(sublime_plugin.EventListener):

    def __init__(self):

        for window in sublime.windows():
            window.run_command("toggle_full_screen")
