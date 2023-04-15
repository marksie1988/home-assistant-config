class Validate:
    """Validate."""

    errors = []

    @property
    def success(self):
        """Return bool if the validation was a success."""
        return not self.errors
