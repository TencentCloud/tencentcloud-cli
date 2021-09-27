**Example 1: 忽略检测项影响主机列表接口**

根据检测项id查询忽略检测项影响主机列表数据

Input: 

```
tccli cwp DescribeIgnoreRuleEffectHostList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --RuleId 1 \
    --TagNames tag
```

Output: 
```
{
    "Response": {
        "IgnoreRuleEffectHostList": [
            {
                "HostName": "测试主机3",
                "Level": "1",
                "TagList": [
                    "展会"
                ],
                "Status": 1,
                "LastScanTime": "2020-06-16 09:13:54",
                "EventId": 666,
                "Quuid": "23220"
            },
            {
                "HostName": "测试主机3",
                "Level": "3",
                "TagList": [
                    "展会"
                ],
                "Status": 1,
                "LastScanTime": "2020-06-16 09:13:54",
                "EventId": 666,
                "Quuid": "23220"
            }
        ],
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "TotalCount": 2
    }
}
```

