from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Digits
from textual.containers import HorizontalGroup
from textual.reactive import Reactive


class CounterDisplay(Digits):
    pass

class Counter(HorizontalGroup):
    """A simple counter component."""
    count = Reactive(0)
    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield CounterDisplay(value=str(self.count), id="counter_display")
        yield Button("Increment", id="increment")
        yield Button("Decrement", id="decrement")
        yield Button("Reset", id="reset")

class CounterApp(App):
    """A simple counter app using Textual."""

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "reset", "Reset"),
        ("t", "toggle_darkmode", "Toggle Dark Mode")
    ]

    CSS_PATH = "counter.tcss"

    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield Header(show_clock=True, icon="")
        yield Counter(id="counter")
        yield Footer()

    def action_toggle_darkmode(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    


if __name__ == "__main__":
    app = CounterApp()
    app.run()