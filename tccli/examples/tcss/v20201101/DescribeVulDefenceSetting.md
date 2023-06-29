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
        "HostIDs": [
            "abc"
        ],
        "HostTotalCount": 0,
        "SupportDefenseVulCount": 0,
        "HostNodeCount": 0,
        "SuperScope": 0,
        "SuperNodeCount": 0,
        "SuperNodeIds": [
            "abc"
        ],
        "NodeTotalCount": 0,
        "RequestId": "abc"
    }
}
```

