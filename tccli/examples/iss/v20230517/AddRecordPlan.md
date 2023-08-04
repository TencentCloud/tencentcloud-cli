**Example 1: 成功**

 

Input: 

```
tccli iss AddRecordPlan --cli-unfold-argument  \
    --PlanName name \
    --TemplateId 48676e89a8c**********baa36220fa4 \
    --Describe abc \
    --StreamType main \
    --Channels.0.DeviceId 48676e89a8c**********baa36220fa4 \
    --Channels.0.ChannelId 9ee325e9984**********a805c19b4e1 \
    --OrganizationId 10 \
    --LifeCycle.Transition 1 \
    --LifeCycle.Expiration 60
```

Output: 
```
{
    "Response": {
        "Data": {
            "PlanId": "88ac5ea6c1f**********24671d0f94f",
            "PlanName": "name",
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "Describe": "abc",
            "StreamType": "main",
            "LifeCycle": {
                "Transition": 1,
                "Expiration": 60
            }
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

