import logging

def get_logger(name: str):
    """
    Central logger factory.

    Why central?
    - Consistent format
    - Easy to upgrade later (ELK, CloudWatch)
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
