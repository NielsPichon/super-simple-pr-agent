def get_diff_from_github() -> str:
    """Get the diff from the GitHub event."""
    raise NotImplementedError()


def publish_review(review: str):
    """Publish the review as a comment on GitHub."""
    raise NotImplementedError()
