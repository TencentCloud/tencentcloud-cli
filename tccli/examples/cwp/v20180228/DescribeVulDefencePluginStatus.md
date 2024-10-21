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
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Alias": "销售许可测试机器",
                "PrivateIp": "10.0.1.15",
                "PublicIp": "xx.xx.xx.xx",
                "Exception": 2,
                "CreateTime": "2024-10-21 19:38:46",
                "ModifyTime": "2024-10-21 19:38:46"
            }
        ],
        "RequestId": "abc"
    }
}
```

