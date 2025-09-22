**Example 1: 新建补录跳过事件**



Input: 

```
tccli wedata CreateDataBackfillPlan --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskIds 20250827115253729 \
    --DataBackfillRangeList.0.StartDate 2025-09-02 \
    --DataBackfillRangeList.0.EndDate 2025-09-02 \
    --SkipEventListening True
```

Output: 
```
{
    "Response": {
        "Data": {
            "DataBackfillPlanId": "0726eb7b-0ffc-4ed7-8be4-2ef189645209"
        },
        "RequestId": "2ba8b5eb-b98f-4ad2-9bab-0960fa346c18"
    }
}
```

