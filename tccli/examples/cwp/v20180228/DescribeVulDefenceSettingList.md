**Example 1: 查询漏洞防御设置列表**

查询漏洞防御设置列表

Input: 

```
tccli cwp DescribeVulDefenceSettingList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 251006279,
                "DefenceType": 0,
                "Enable": 0,
                "InstanceNum": 0,
                "MemberId": "",
                "Nickname": "",
                "Scope": 1,
                "StrategyAction": 1,
                "StrategyName": "漏洞防御",
                "StrategyType": 0,
                "SupportVulNum": 150,
                "ThreatLevel": 4,
                "Uin": ""
            },
            {
                "AppId": 251006279,
                "DefenceType": 1,
                "Enable": 0,
                "InstanceNum": 0,
                "MemberId": "",
                "Nickname": "",
                "Scope": 1,
                "StrategyAction": 0,
                "StrategyName": "网络攻击",
                "StrategyType": 0,
                "SupportVulNum": 231,
                "ThreatLevel": 4,
                "Uin": ""
            }
        ],
        "RequestId": "d4a7d250-c0c0-4f57-9416-6926f98fc02f",
        "TotalCount": 2
    }
}
```

