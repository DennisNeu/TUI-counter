from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer


class CounterApp(App):
    """A simple counter app using Textual."""
    counter = 0

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "reset", "Reset"),
        ("i", "increment", "Increment"),
        ("d", "decrement", "Decrement"),
    ]

    CSS_PATH = "counter.tcss"

    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield Header(show_clock=True, icon="")
        yield Button("Increment", id="increment")
        yield Button("Decrement", id="decrement")
        yield Button("Reset", id="reset")
        yield Footer()


if __name__ == "__main__":
    app = CounterApp()
    app.run()