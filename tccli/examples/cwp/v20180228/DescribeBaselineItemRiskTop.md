**Example 1: 检测项top5**



Input: 

```
tccli cwp DescribeBaselineItemRiskTop --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "718b3dda-c0a7-409c-84bd-712411880bbe",
        "RiskItemTop5": [
            {
                "ItemId": 1505,
                "ItemName": "Linux口令过期后账号最长有效天数策略",
                "Level": 2,
                "HostCount": 31
            },
            {
                "ItemId": 1509,
                "ItemName": "限制root权限用户远程登录",
                "Level": 2,
                "HostCount": 31
            },
            {
                "ItemId": 1500,
                "ItemName": "SSH监听在默认端口",
                "Level": 1,
                "HostCount": 31
            },
            {
                "ItemId": 5275,
                "ItemName": "检查SSH的root用户登录是否被禁用",
                "Level": 3,
                "HostCount": 22
            },
            {
                "ItemId": 5273,
                "ItemName": "检查账户超时自动登出设置",
                "Level": 2,
                "HostCount": 22
            }
        ]
    }
}
```

