**Example 1: 失败示例**

包含无效的通道ID

Input: 

```
tccli iss AddAITask --cli-unfold-argument  \
    --Name ai-task \
    --Desc 测试 \
    --ChannelList ********************** \
    --CallbackUrl http://******* \
    --Templates.0.Tag AI \
    --Templates.0.AIConfig.DetectType Pet \
    --Templates.0.AIConfig.TimeInterval 10 \
    --Templates.0.AIConfig.OperTimeSlot.0.Start 10:00:00 \
    --Templates.0.AIConfig.OperTimeSlot.0.End 20:00:00
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.ContainInvalidChannelId",
            "Message": "包含无效的通道ID"
        },
        "RequestId": "d380c0bc-2be1-4620-bf39-9d4d4f512060"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss AddAITask --cli-unfold-argument  \
    --Name ai-task \
    --Desc 测试 \
    --ChannelList 97308958-6122-4188-8c78-d5ff8010bdf7 \
    --CallbackUrl http://********** \
    --Templates.0.Tag AI \
    --Templates.0.AIConfig.DetectType Pet \
    --Templates.0.AIConfig.TimeInterval 10 \
    --Templates.0.AIConfig.OperTimeSlot.0.Start 10:00:00 \
    --Templates.0.AIConfig.OperTimeSlot.0.End 20:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "CallbackUrl": "http://**********",
            "ChannelList": [
                "**********************"
            ],
            "CreatedTime": "2023-06-15 15:50:47",
            "Desc": "测试",
            "Name": "ai-task",
            "Status": "off",
            "TaskId": "at**********************8",
            "Templates": [
                {
                    "AIConfig": {
                        "DetectType": "Pet",
                        "OperTimeSlot": [
                            {
                                "End": "20:00:00",
                                "Start": "10:00:00"
                            }
                        ],
                        "TimeInterval": 10
                    },
                    "Tag": "AI"
                }
            ],
            "UpdatedTime": "2023-06-15 15:50:47"
        },
        "RequestId": "4ea417f6-da0e-4211-9b97-6408070b9851"
    }
}
```

