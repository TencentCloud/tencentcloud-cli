**Example 1: 删除规则组**

删除规则组

Input: 

```
tccli wedata DeleteQualityRuleGroup --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --RuleGroupIdList 677
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailedCount": 0,
            "Results": [
                {
                    "Id": 677,
                    "Msg": null,
                    "Name": "employee_202505141709",
                    "Success": true
                }
            ],
            "SuccessCount": 0,
            "SumCount": 0
        },
        "RequestId": "ab686dad-4259-4fb3-aec9-3630064bb3e8"
    }
}
```

