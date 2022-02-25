from typing import List, Optional

from discord import Guild, Role


class Project:
    def __init__(self, name: str, provider_name: str, project_id: str, auth_config: any):
        self.name = name
        self.provider_name = provider_name
        self.project_id = project_id
        self.auth_config = auth_config


class Config:
    def __init__(
            self,
            user_role: Optional[Role],
            admin_role: Optional[Role],
            projects: List[Project]
    ):
        self.user_role = user_role
        self.admin_role = admin_role
        self.projects = projects


class ConfigPool:
    _pool = []

    @classmethod
    def get(cls, guild: Guild) -> Config:
        pass  # todo

    @classmethod
    def save(cls, guild: Guild, config: Config):
        pass  # todo
