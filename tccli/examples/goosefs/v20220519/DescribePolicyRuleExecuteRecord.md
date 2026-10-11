**Example 1: 查询执行记录**



Input: 

```
tccli goosefs DescribePolicyRuleExecuteRecord --cli-unfold-argument  \
    --FileSystemId x-c60-0q62fdo7 \
    --Offset 0 \
    --Limit 10 \
    --RuleId 1786019949985
```

Output: 
```
{
    "Response": {
        "RuleExecuteList": [
            {
                "Capacity": 588,
                "EndTime": "2026-08-06T20:40:11+08:00",
                "FileCount": 111105,
                "ManifestUrl": "https://goosefsx-test-**********.cos.ap-shanghai.myqcloud.com/policy/scan_policy_all_1786019949985_1786020001688.list.gfsx",
                "RecordId": "1786020001688",
                "StartTime": "2026-08-06T20:40:06+08:00",
                "Status": 2
            }
        ],
        "TotalCount": 1,
        "RequestId": "b0cde05c-ef51-4489-9999-6031a4921e02"
    }
}
```

