from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Digits
from textual.containers import HorizontalGroup
from textual.reactive import Reactive


class CounterDisplay(Digits):
    pass


class Counter(HorizontalGroup):
    """A simple counter component."""
    count = Reactive(1)

    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield CounterDisplay(value=str(self.count), id="counter_display")
        yield Button("Increment", id="increment", variant="success")
        yield Button("Decrement", id="decrement", variant="error")
        yield Button("Reset", id="reset")

    def on_mount(self) -> None:
        """Set up reactivity."""
        self.watch(self, 'count', self.update_display)

    def update_display(self, count: int) -> None:
        """Update the counter display when count changes."""
        display = self.query_one("#counter_display", CounterDisplay)
        display.update(str(count))

    def increment(self) -> None:
        """Increment the counter."""
        self.count += 1
        print(self.count)
        
    def decrement(self) -> None:
        """Decrement the counter."""
        self.count -= 1

    def reset(self) -> None:
        """Reset the counter."""
        self.count = 0

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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        counter = self.query_one(Counter)
        if event.button.id == "increment":
            counter.increment()
        elif event.button.id == "decrement":
            counter.decrement()
        elif event.button.id == "reset":
            counter.reset()


if __name__ == "__main__":
    app = CounterApp()
    app.run()