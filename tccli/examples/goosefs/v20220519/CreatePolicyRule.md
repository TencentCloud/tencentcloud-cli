**Example 1: 创建扫描规则**



Input: 

```
tccli goosefs CreatePolicyRule --cli-unfold-argument  \
    --FileSystemId x-c60-0q62fdo7 \
    --ScanDir /test_policy/ \
    --Name policy_now \
    --Execution.ExecuteMode scheduled \
    --Execution.ExecuteAt 2026-08-06T21:30:00 \
    --Execution.WaitTime 12 \
    --PolicyRuleSet.0.Key FILE_SIZE \
    --PolicyRuleSet.0.Operator > \
    --PolicyRuleSet.0.Value 0 \
    --EnableManifest True \
    --Manifest.Bucket goosefsx-test-1252246555 \
    --Manifest.Prefix policy \
    --Manifest.Attributes FILE_SIZE \
    --Manifest.Region ap-shanghai
```

Output: 
```
{
    "Response": {
        "RuleId": "1786020012996",
        "RequestId": "4c328927-f95e-40f0-9e14-2462a19e4027"
    }
}
```

