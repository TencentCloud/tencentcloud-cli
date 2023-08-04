**Example 1: 成功**

 

Input: 

```
tccli iss DescribeRecordPlan --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f
```

Output: 
```
{
    "Response": {
        "Data": {
            "ChannelCount": 1,
            "PlanId": "88ac5ea6c1**********224671d0f94f",
            "PlanName": "name1",
            "TemplateId": "9ee325e9984b**********805c19b4e1",
            "Describe": "",
            "StreamType": "main",
            "LifeCycle": {
                "Transition": 10,
                "Expiration": 60
            },
            "Status": 1
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

