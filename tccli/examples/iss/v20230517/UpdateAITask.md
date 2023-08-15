**Example 1: 失败示例**

AI任务不存在

Input: 

```
tccli iss UpdateAITask --cli-unfold-argument  \
    --TaskId at**********************1 \
    --Desc 111
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.AITaskNotExisted",
            "Message": "AI任务不存在"
        },
        "RequestId": "7954b883-9141-4635-b116-4be839cfd810"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss UpdateAITask --cli-unfold-argument  \
    --TaskId at**********************8 \
    --Desc 111
```

Output: 
```
{
    "Response": {
        "Data": {
            "CallbackUrl": "http://********",
            "ChannelList": [
                "**********************"
            ],
            "CreatedTime": "2023-06-15 16:21:34",
            "Desc": "111",
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
            "UpdatedTime": "2023-06-15 16:21:34"
        },
        "RequestId": "b78d57bf-7742-4048-80c1-11709aaf14bf"
    }
}
```

