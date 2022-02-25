from abc import ABC, abstractmethod
from typing import Optional

AuthConfig = any


class AuthRegisterRequest:
    """An (unfinished?) authentication request for adding a new project"""
    def __init__(self, url: str, internal_information: any = None):
        # The URL used for querying the User for OAuth permission.
        self.url = url
        # Internal notes to keep track of the request, optional and provider-dependant.
        self.internal_information = internal_information
        # JSON serializable configuration to store in the project configuration file
        # AFTER the authentication is done. This must be set in finish_register_project.
        self.auth_config: AuthConfig = None


class AbstractProvider(ABC):
    @abstractmethod
    def friendly_name(self):
        """The human-readable friendly name of this provider."""

    @abstractmethod
    def description(self):
        """The human-readable friendly description of this provider."""

    @abstractmethod
    def id_usage(self):
        """The human-readable friendly explanation of what project ID is for this provider
        (eg. Github org/user, Trello board ID, etc.)."""

    @abstractmethod
    async def request_register_project(self, url: str) -> AuthRegisterRequest:
        """
        Registers a project to the list of registered repositories using the provided project ID,
        can raise any error. How the ID must be structured is up to the provider.
        Returns the request object for keeping track of this request later, when
        finishing the authentication and also for providing the URL to be given to the user for the OAuth
        request.
        """

    @abstractmethod
    async def finish_register_project(self, context: any, token: str) -> Optional[AuthRegisterRequest]:
        """
        Finish a project registration using the provided context in the answer parameters
        of the OAuth authentication. Can raise any error. How the context is structured depends on the
        answer of the authentication.
        Returns the same request object as used with request_register_project and provides an auth_config
        in it.
        Returns None if the request didn't match any known registration request.
        """

    @abstractmethod
    async def create_issue(self, auth_config: AuthConfig, title: str, description: str) -> Optional[str]:
        """
        Create an issue with the given title and description, can raise any error.
        On success returns the created issue URL or None if n/a.
        """
