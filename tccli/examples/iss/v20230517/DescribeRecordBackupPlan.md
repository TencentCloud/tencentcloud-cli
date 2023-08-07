**Example 1: 成功**

 

Input: 

```
tccli iss DescribeRecordBackupPlan --cli-unfold-argument  \
    --PlanId hijklmno-efgh-5678-ijkl-1234567890ab
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
                "Transition": 7
            },
            "PlanId": "hijklmno-efgh-5678-ijkl-1234567890ab",
            "PlanName": "test-plan-update",
            "Status": 1,
            "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
            "UpdateAt": "2023-06-05 15:05:25"
        },
        "RequestId": "1c508daa-c317-4e17-b313-79761aa81a6b"
    }
}
```

