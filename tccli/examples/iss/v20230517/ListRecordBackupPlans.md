**Example 1: 成功**

 

Input: 

```
tccli iss ListRecordBackupPlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ChannelCount": 0,
                "CreateAt": "2023-06-05 14:32:04",
                "Describe": "test",
                "LifeCycle": {
                    "Expiration": 0,
                    "Transition": 7
                },
                "PlanId": "hijklmno-efgh-5678-ijkl-1234567890ab",
                "PlanName": "test-plan-update",
                "Status": 1,
                "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
                "UpdateAt": "2023-06-05 14:56:51"
            }
        ],
        "RequestId": "4427b009-03b4-42d9-ae3a-4bdf1582df4f"
    }
}
```

