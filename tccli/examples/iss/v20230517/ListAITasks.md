**Example 1: 失败示例**

无效的分页大小

Input: 

```
tccli iss ListAITasks --cli-unfold-argument  \
    --IsContainChannelList True \
    --IsContainTemplate True \
    --PageNumber 1 \
    --PageSize 201
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidPageSize",
            "Message": "无效的分页大小"
        },
        "RequestId": "f334da88-758f-43de-a0ae-f736c9c905ff"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss ListAITasks --cli-unfold-argument  \
    --IsContainChannelList True \
    --IsContainTemplate True
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "CallbackUrl": "http://********",
                    "ChannelList": [
                        "**********************"
                    ],
                    "CreatedTime": "2023-06-07 00:35:36",
                    "Desc": "AI任务描述",
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
                    "UpdatedTime": "2023-06-07 00:35:36"
                }
            ]
        },
        "RequestId": "a9227772-9f97-4ec8-88bd-a1991b1363d4",
        "TotalCount": 1
    }
}
```

