**Example 1: 获取当前漏洞防御插件设置**



Input: 

```
tccli cwp DescribeVulDefenceSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "Enable": 1,
        "Scope": 0,
        "Quuids": [
            "d92d723e-4aac-4f4a-bbf9-e5430e29d289"
        ],
        "FlagshipCount": 8
    }
}
```

