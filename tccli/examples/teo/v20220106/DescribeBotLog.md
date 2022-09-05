**Example 1: 查询Bot攻击日志**



Input: 

```
tccli teo DescribeBotLog --cli-unfold-argument  \
    --PageSize 1 \
    --PageNo 1 \
    --ZoneIds zone-21xfqlh4qjee \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value monitor \
    --QueryCondition.0.Key action \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "success",
        "Data": {
            "TotalSize": 1,
            "List": [
                {
                    "AttackContent": "",
                    "AttackIp": "120.241.137.74",
                    "AttackTime": 1660035802,
                    "Domain": "cooper5.wshxin.cn",
                    "EventId": "91558071885490496",
                    "Label": "none",
                    "RequestMethod": "GET",
                    "RequestUri": "/",
                    "RuleDetailList": [
                        {
                            "Action": "drop",
                            "Description": "营销",
                            "RuleId": 1003,
                            "RuleTypeName": "uabot"
                        }
                    ],
                    "SipCountryCode": "CN",
                    "Ua": "SemrushBot"
                }
            ],
            "PageSize": 1,
            "PageNo": 1,
            "Pages": 1
        },
        "RequestId": "40b7844d-e4d9-4072-824d-f3a8bc85b487"
    }
}
```

