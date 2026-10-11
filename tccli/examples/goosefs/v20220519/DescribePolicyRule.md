**Example 1: 列出扫描规则**



Input: 

```
tccli goosefs DescribePolicyRule --cli-unfold-argument  \
    --FileSystemId x-c60-0q62fdo7 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PolicyRuleTaskList": [
            {
                "CreateTime": "2026-08-06T20:40:12+08:00",
                "EnableManifest": true,
                "Execution": {
                    "ExecuteAt": "2026-08-06T21:30:00",
                    "ExecuteMode": "scheduled",
                    "ExecutePeriod": null,
                    "WaitTime": 12
                },
                "Manifest": {
                    "Attributes": [
                        "FILE_SIZE"
                    ],
                    "Bucket": "goosefsx-test-1252246555",
                    "Prefix": "policy",
                    "Region": "ap-shanghai"
                },
                "ModifyTime": "2026-08-06T20:40:12+08:00",
                "Name": "policy_now",
                "PolicyRuleSet": [
                    {
                        "Key": "FILE_SIZE",
                        "Operator": ">",
                        "Value": "0"
                    }
                ],
                "RuleId": "1786020012996",
                "ScanDir": "/test_policy/",
                "Status": 0
            }
        ],
        "TotalCount": 11,
        "RequestId": "0fbfbc3a-9d33-47e1-85af-b846e93a157f"
    }
}
```

