**Example 1: 无实时上云计划**

 

Input: 

```
tccli iss ListRecordPlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 有实时上云计划**

 

Input: 

```
tccli iss ListRecordPlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
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
            {
                "ChannelCount": 1,
                "PlanId": "bf3a4476c7b4**********e8dcb62351",
                "PlanName": "name2",
                "TemplateId": "48676e89a8c1**********aa36220fa4",
                "Describe": "",
                "StreamType": "main",
                "LifeCycle": {
                    "Transition": 10,
                    "Expiration": 60
                },
                "Status": 0
            }
        ],
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

