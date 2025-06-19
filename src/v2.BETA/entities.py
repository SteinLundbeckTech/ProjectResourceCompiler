"""
    @Date                 : 19.06.2025
    @Author               : Stein Lundbeck
    @Name                 : PRC entities
    @Description          : Different entities used in the PRC tool
    @Version              : 1.0.0.1
    @Latest               : 19.06.2025
"""

import json

class Project:
    """Represents a project loaded from config"""
    def __init__(self, project, index):
        self.project = project
        self.index = index
        self.name = project["name"]
        self.path = project["path"]
        self.actions = project["actions"]

class Defaults:
    """All default values"""
    def __init__(self):
        self.json = None
        self.values = None

    def load(self):
        """Loads default values from config file"""
        with open("Config.json", encoding="utf-8") as val:
            self.json = val
            self.values = json.load(val)["default"]
            print(self.values)

    def get(self, key):
        """Gets a default value by key"""
        result = None
        for n, v in self.values.items():
            if n == key:
                result = v
                break
        if not result:
            for path in self.values["default"]["paths"]:
                if path["name"] == key:
                    result = path["value"]
                    break
        if not result:
            raise ValueError(f"Default value with key '{key}' not found")
        return result

class ActionBase:
    """Base class for project actions"""
    def __init__(self, project, action_type):
        self.project = project
        self.action_type = action_type
        self.defaults = Defaults()
        match action_type:
            case "STYLE":
                self.action = StyleAction(project)
                self.enabled = self.defaults.get("styleEnabled")
            case "SCRIPT":
                self.action = ScriptAction(project)
                self.enabled = self.defaults.get("scriptEnabled")
            case "IMAGE":
                self.action = ImageAction(project)
                self.enabled = self.defaults.get("imageEnabled")
            case "DISTRO":
                self.action = DistroAction(project)
                self.enabled = self.defaults.get("distroEnabled")
            case _:
                raise ValueError(f"Unknown action type: {action_type}")

class StyleAction(ActionBase):
    """Represents style action"""
    def __init__(self, project):
        super().__init__(project, "STYLE")
        self.enabled = True

class ScriptAction(ActionBase):
    """Represents script action"""
    def __init__(self, project):
        super().__init__(project, "SCRIPT")
        self.enabled = True

class ImageAction(ActionBase):
    """Represents image action"""
    def __init__(self, project):
        super().__init__(project, "IMAGE")
        self.enabled = True

class DistroAction(ActionBase):
    """Represents distro action"""
    def __init__(self, project):
        super().__init__(project, "DISTRO")
        self.enabled = True
