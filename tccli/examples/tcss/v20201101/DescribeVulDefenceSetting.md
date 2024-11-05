**Example 1: 查询漏洞防御设置信息**

查询漏洞防御设置信息

Input: 

```
tccli tcss DescribeVulDefenceSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsEnabled": 0,
        "Scope": 0,
        "HostCount": 0,
        "ExceptionHostCount": 0,
        "HostIDs": [],
        "HostTotalCount": 0,
        "SupportDefenseVulCount": 0,
        "HostNodeCount": 0,
        "SuperScope": 0,
        "SuperNodeCount": 0,
        "SuperNodeIds": [],
        "NodeTotalCount": 0,
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

