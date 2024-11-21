**Example 1: getescapeRule**



Input: 

```
tccli tcss DescribeEscapeRuleInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d8663c94-1030-4256-8e10-a3822d7b5e10",
        "RuleSet": [
            {
                "Group": "PROCESS_PRIVILEGE",
                "IsEnable": true,
                "Name": "突破namespace限制",
                "Type": "PRIVILEGE"
            },
            {
                "Group": "RISK_CONTAINER",
                "IsEnable": true,
                "Name": "敏感路径挂载",
                "Type": "MOUNT_SENSITIVE_PTAH"
            },
            {
                "Group": "CONTAINER_ESCAPE",
                "IsEnable": true,
                "Name": "逃逸漏洞利用",
                "Type": "ESCAPE_VUL_OCCURRED"
            },
            {
                "Group": "CONTAINER_ESCAPE",
                "IsEnable": true,
                "Name": "访问Docker API接口逃逸",
                "Type": "ESCAPE_DOCKER_API"
            },
            {
                "Group": "CONTAINER_ESCAPE",
                "IsEnable": true,
                "Name": "篡改敏感文件逃逸",
                "Type": "ESCAPE_TAMPER_SENSITIVE_FILE"
            },
            {
                "Group": "CONTAINER_ESCAPE",
                "IsEnable": true,
                "Name": "利用cgroup机制逃逸",
                "Type": "ESCAPE_CGROUPS"
            }
        ]
    }
}
```

