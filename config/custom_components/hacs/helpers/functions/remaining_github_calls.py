"""Helper to calculate the remaining calls to github."""
import math

from custom_components.hacs.helpers.functions.logger import getLogger


async def remaining(github):
    """Helper to calculate the remaining calls to github."""
    logger = getLogger("custom_components.hacs.remaining_github_calls")
    try:
        ratelimits = await github.get_rate_limit()
    except BaseException as exception:
        logger.error(exception)
        return None
    if ratelimits.get("remaining") is not None:
        return int(ratelimits["remaining"])
    return 0


async def get_fetch_updates_for(github):
    """Helper to calculate the number of repositories we can fetch data for."""
    limit = await remaining(github)
    if limit is None:
        return None

    margin = 100
    pr_repo = 10

    return (
        0
        if limit - margin <= pr_repo
        else math.floor((limit - margin) / pr_repo)
    )
