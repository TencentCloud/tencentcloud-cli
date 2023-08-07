**Example 1: 成功**

 

Input: 

```
tccli iss AddRecordBackupPlan --cli-unfold-argument  \
    --TemplateId abcdefgh-1234-5678-ijkl-1234567890ab \
    --PlanName test-plan-1 \
    --Describe test1 \
    --LifeCycle.Transition 7 \
    --LifeCycle.Expiration 0 \
    --OrganizationId 191
```

Output: 
```
{
    "Response": {
        "Data": {
            "ChannelCount": 0,
            "CreateAt": "2023-06-05 15:11:43",
            "Describe": "test1",
            "LifeCycle": {
                "Expiration": 0,
                "Transition": 7
            },
            "PlanId": "hijklmno-efgh-5678-ijkl-1234567890ab",
            "PlanName": "test-plan-1",
            "Status": 0,
            "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
            "UpdateAt": "2023-06-05 15:11:43"
        },
        "RequestId": "b00b406c-b891-4ef0-9169-16dc4c51e8a9"
    }
}
```

