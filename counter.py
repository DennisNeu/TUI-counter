from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Digits
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import Reactive


class CounterDisplay(Digits):
    pass


class Counter(HorizontalGroup):
    """A simple counter component."""
    count = Reactive(0)

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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "increment":
            self.increment()
        elif event.button.id == "decrement":
            self.decrement()
        elif event.button.id == "reset":
            self.reset()


class CounterApp(App):
    """A simple counter app using Textual."""

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("a", "add", "Add"),
        ("r", "remove", "Remove"),
        ("t", "toggle_darkmode", "Toggle Dark Mode")
    ]

    CSS_PATH = "counter.tcss"

    def compose(self) -> ComposeResult:
        """Create the UI components."""
        yield Header(show_clock=True, icon="")
        # yield Counter(id="counter")
        yield VerticalScroll(Counter(), id="counters")
        yield Footer()
    
    def action_add(self) -> None:
        """An action to add a new counter."""
        new_counter = Counter()
        self.query_one("#counters").mount(new_counter)
        new_counter.scroll_visible()


    def action_remove(self) -> None:
        """Called to remove a counter."""
        counters = self.query("Counter")
        if counters:
            counters.last().remove()


    def action_toggle_darkmode(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = CounterApp()
    app.run()