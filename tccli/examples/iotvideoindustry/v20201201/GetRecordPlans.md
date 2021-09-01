**Example 1: 获取全部录制计划**



Input: 

```
tccli iotvideoindustry GetRecordPlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Plans": [
            {
                "PlanId": "plan-yhp5zzq9",
                "Name": "myPlan",
                "TimeTemplateId": "tgrp-a6gvpkzu",
                "TimeTemplateName": "myTimeTemplate",
                "EventId": 1,
                "Devices": []
            }
        ],
        "RequestId": "c6cc4efc-a7db-4c93-a373-0ce2a383023a",
        "TotalCount": 1
    }
}
```

