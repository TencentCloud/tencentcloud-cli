**Example 1: 修改计划名称**

 

Input: 

```
tccli iss UpdateRecordPlan --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --Mod.PlanName newname
```

Output: 
```
{
    "Response": {
        "Data": {
            "PlanId": "88ac5ea6c1f**********24671d0f94f",
            "PlanName": "newname",
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "Describe": "",
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

**Example 2: 修改计划模板**

  

Input: 

```
tccli iss UpdateRecordPlan --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --Mod.TemplateId 48676e89a8c**********baa36a87832
```

Output: 
```
{
    "Response": {
        "Data": {
            "PlanId": "88ac5ea6c1f**********24671d0f94f",
            "PlanName": "name",
            "TemplateId": "48676e89a8c**********baa36a87832",
            "Describe": "",
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

**Example 3: 删除计划通道**

 

Input: 

```
tccli iss UpdateRecordPlan --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --Mod.Del 9ee325e9984**********a805c19b4e1
```

Output: 
```
{
    "Response": {
        "Data": {
            "PlanId": "88ac5ea6c1f**********24671d0f94f",
            "PlanName": "name",
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "Describe": "",
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

**Example 4: 增加计划通道**

 

Input: 

```
tccli iss UpdateRecordPlan --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --Mod.Add.0.DeviceId 9ee325e9984**********a805c19b4e1 \
    --Mod.Add.0.ChannelId 48676e89a8c**********baa36220fa4
```

Output: 
```
{
    "Response": {
        "Data": {
            "PlanId": "88ac5ea6c1f**********24671d0f94f",
            "PlanName": "name",
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "Describe": "",
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

**Example 5: 修改计划生命周期**

 

Input: 

```
tccli iss UpdateRecordPlan --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --Mod.LifeCycle.Transition 7 \
    --Mod.LifeCycle.Expiration 80
```

Output: 
```
{
    "Response": {
        "Data": {
            "PlanId": "88ac5ea6c1f**********24671d0f94f",
            "PlanName": "name",
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "Describe": "",
            "StreamType": "main",
            "LifeCycle": {
                "Transition": 7,
                "Expiration": 80
            }
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

