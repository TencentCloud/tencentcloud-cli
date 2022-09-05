**Example 1: 查询CC防护日志**



Input: 

```
tccli teo DescribeWebProtectionLog --cli-unfold-argument  \
    --PageSize 1 \
    --PageNo 1 \
    --EntityType acl \
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
        "Msg": "xx",
        "Data": {
            "TotalSize": 0,
            "List": [
                {
                    "EventId": "91558071885490496",
                    "SipCountryCode": "CN",
                    "RequestUri": "/",
                    "RequestMethod": "GET",
                    "RuleDetailList": [
                        {
                            "Description": "cooper5_acl",
                            "RuleId": 1123,
                            "RuleTypeName": "cooper5_acl",
                            "Action": "monitor"
                        }
                    ],
                    "AttackDomain": "www.baidu.com",
                    "AttackTime": 1660035802,
                    "DisposalMethod": "xx",
                    "HitCount": 1,
                    "Ua": "SemrushBot",
                    "AttackSip": "1.2.3.4"
                }
            ],
            "PageSize": 1,
            "PageNo": 1,
            "Pages": 1
        },
        "RequestId": "a55ce448-d5e6-4351-9a1f-8f0a5222fba1"
    }
}
```

