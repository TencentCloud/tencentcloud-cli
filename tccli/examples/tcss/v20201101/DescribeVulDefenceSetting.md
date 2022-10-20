**Example 1: 查询漏洞防御设置信息**



Input: 

```
tccli tcss DescribeVulDefenceSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsEnabled": 0,
        "SupportDefenseVulCount": 0,
        "RequestId": "xx",
        "Scope": 0,
        "HostIDs": [
            "xx"
        ],
        "ExceptionHostCount": 0,
        "HostCount": 0,
        "HostTotalCount": 0
    }
}
```

