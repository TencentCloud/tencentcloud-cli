**Example 1: 测试用例**



Input: 

```
tccli waf CreateAndUpdateBatchCCRule --cli-unfold-argument  \
    --Name batch-test-cc-0 \
    --RuleId 0 \
    --Status 1 \
    --Advance 1 \
    --Limit 3 \
    --Interval 60 \
    --ActionType 22 \
    --Priority 50 \
    --ValidTime 600 \
    --SessionApplied 2000000577 \
    --LogicalOp and \
    --ActionRatio 100 \
    --PageId 0 \
    --GroupIds 8500001558 \
    --JobType TimedJob \
    --JobDateTime.Timed.0.StartDateTime 0 \
    --JobDateTime.Timed.0.EndDateTime 0 \
    --JobDateTime.TimeTZone UTC+8
```

Output: 
```
{
    "Response": {
        "Data": "",
        "RuleId": 1900037478,
        "RequestId": "aee526df-4ce6-451a-8d39-cce39ed2e46c"
    }
}
```

