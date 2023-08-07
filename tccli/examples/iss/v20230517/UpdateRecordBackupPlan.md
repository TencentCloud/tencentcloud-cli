**Example 1: 成功**

 

Input: 

```
tccli iss UpdateRecordBackupPlan --cli-unfold-argument  \
    --PlanId hijklmno-efgh-5678-ijkl-1234567890ab \
    --Mod.PlanName test-plan-update
```

Output: 
```
{
    "Response": {
        "Data": {
            "ChannelCount": 0,
            "CreateAt": "2023-06-05 14:32:04",
            "Describe": "test",
            "LifeCycle": {
                "Expiration": 0,
                "Transition": 0
            },
            "PlanId": "hijklmno-efgh-5678-ijkl-1234567890ab",
            "PlanName": "test-plan-update",
            "Status": 1,
            "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
            "UpdateAt": "2023-06-05 15:05:25"
        },
        "RequestId": "6428c72b-e6aa-47f2-9062-a24e35a69da6"
    }
}
```

