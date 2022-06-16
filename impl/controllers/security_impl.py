import logging

from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials

from libs import config_loader

logger = logging.getLogger(__name__)
config = config_loader.Config()


def get_token_bearerAuth(authorization_credentials: HTTPAuthorizationCredentials):
    logger.info(f"Received authorization credentials: {authorization_credentials}")

    if authorization_credentials.credentials != config.get(config_loader.API_KEY):
        logger.warning(
            f"Unknown authorization credentials: {authorization_credentials}"
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"user": "api"}
