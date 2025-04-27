from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer
from textual.containers import HorizontalGroup


class CounterButtons(HorizontalGroup):
    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield Button("Increment", id="increment")
        yield Button("Decrement", id="decrement")
        yield Button("Reset", id="reset")

class CounterApp(App):
    """A simple counter app using Textual."""
    counter = 0

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "reset", "Reset"),
        ("i", "increment", "Increment"),
        ("d", "decrement", "Decrement"),
        ("t", "toggle_darkmode", "Toggle Dark Mode")
    ]

    CSS_PATH = "counter.tcss"

    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield Header(show_clock=True, icon="")
        yield CounterButtons()
        yield Footer()

    def action_toggle_darkmode(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = CounterApp()
    app.run()