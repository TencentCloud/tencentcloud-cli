**Example 1: 创建快照策略**



Input: 

```
tccli cfs CreateAutoSnapshotPolicy --cli-unfold-argument  \
    --Hour 1 \
    --PolicyName abd \
    --DayOfWeek 1 \
    --AliveDays 1 \
    --ResourceTags.0.TagKey u90e8u95e8 \
    --ResourceTags.0.TagValue u4e91u4ea7u54c1u4e00u90e8
```

Output: 
```
{
    "Response": {
        "AutoSnapshotPolicyId": "asp-fglw8r91",
        "RequestId": "0c37adaf-f6bc-4fca-b387-454ea93127e1"
    }
}
```

