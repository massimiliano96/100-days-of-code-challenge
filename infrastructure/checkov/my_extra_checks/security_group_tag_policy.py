from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories
from typing import Any, Dict

class CheckSecurityGroupTags(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure all security groups have the tag 'name' equal to 'custom-tag-for-security-group'"
        id = "CUSTOM_AWS_1"
        supported_resources = ("aws_security_group",)
        categories = (CheckCategories.CONVENTION,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
        """
        Looks for the tag 'name' with value 'custom-tag-for-security-group' in aws_security_group configuration.
        :param conf: aws_security_group configuration
        :return: <CheckResult>
        """
        if 'tags' in conf.keys():
            tags = conf.get("tags")
            if tags and isinstance(tags, list):
                tags = tags[0]
                if tags.get("name") == "custom-tag-for-security-group":
                    return CheckResult.PASSED
        return CheckResult.FAILED

check = CheckSecurityGroupTags()