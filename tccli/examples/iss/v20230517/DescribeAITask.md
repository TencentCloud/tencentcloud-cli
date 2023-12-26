**Example 1: 失败示例**

AI任务不存在

Input: 

```
tccli iss DescribeAITask --cli-unfold-argument  \
    --TaskId at**********************1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.AITaskNotExisted",
            "Message": "AI任务不存在"
        },
        "RequestId": "da8025b4-81ee-45ac-b834-b7c0b1665c88"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss DescribeAITask --cli-unfold-argument  \
    --TaskId atc**********************8
```

Output: 
```
{
    "Response": {
        "Data": {
            "CallbackUrl": "http://*******",
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
        "RequestId": "971360c6-adf5-4845-9202-fd43f13ae0ba"
    }
}
```

