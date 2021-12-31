**Example 1: 获取直播录制计划详情**



Input: 

```
tccli iotvideoindustry DescribeLiveRecordPlanById --cli-unfold-argument  \
    --PlanId plan-001
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "PlanName": "直播录制001",
        "TemplateId": "template-001",
        "TemplateName": "录制模板001",
        "RecordStorageTime": 30,
        "PlanType": 2
    }
}
```

