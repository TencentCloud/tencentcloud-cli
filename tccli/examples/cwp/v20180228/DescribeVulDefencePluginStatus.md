**Example 1: 获取各主机漏洞防御插件状态**

获取各主机漏洞防御插件状态

Input: 

```
tccli cwp DescribeVulDefencePluginStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Quuid": "abc",
                "Alias": "abc",
                "PrivateIp": "abc",
                "PublicIp": "abc",
                "Exception": 0,
                "CreateTime": "abc",
                "ModifyTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

