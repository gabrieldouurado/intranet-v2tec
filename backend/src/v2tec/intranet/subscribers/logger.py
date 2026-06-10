from v2tec.intranet import logger
from zope.interface import Interface
from zope.interface.interfaces import IObjectEvent


DEBUG = False


def debug_logs(obj: Interface, event: IObjectEvent):
    """Log events for debugging purposes."""
    if DEBUG:
        logger.info(f"Event: {event}, Object: {obj}")
