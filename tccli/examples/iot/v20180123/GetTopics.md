**Example 1: 获取Topic列表**

获取Topic列表

Input: 

```
tccli iot GetTopics --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --Offset 2 \
    --Length 2
```

Output: 
```
{
    "Response": {
        "RequestId": "afcdaa08-8bb7-4015-999d-57bd8276eeea",
        "Topics": [
            {
                "TopicId": "topic-1ciaft9m",
                "TopicName": "new-topic-3",
                "ProductId": "iot-4e0wsxpi",
                "MsgLife": 86400,
                "MsgSize": 65536,
                "MsgCount": 1000000,
                "Deleted": 0,
                "CreateTime": "2018-03-12 20:33:23",
                "UpdateTime": "2018-03-12 20:33:23",
                "Path": "iot-4e0wsxpi/${device_name}/new-topic-3"
            },
            {
                "TopicId": "topic-mhfrckio",
                "TopicName": "new-topic-2",
                "ProductId": "iot-4e0wsxpi",
                "MsgLife": 86400,
                "MsgSize": 65536,
                "MsgCount": 1000000,
                "Deleted": 0,
                "CreateTime": "2018-03-12 20:33:21",
                "UpdateTime": "2018-03-12 20:33:21",
                "Path": "iot-4e0wsxpi/${device_name}/new-topic-2"
            },
            {
                "TopicId": "topic-7gjao342",
                "TopicName": "new-topic-1",
                "ProductId": "iot-4e0wsxpi",
                "MsgLife": 86400,
                "MsgSize": 65536,
                "MsgCount": 1000000,
                "Deleted": 0,
                "CreateTime": "2018-03-12 20:32:47",
                "UpdateTime": "2018-03-12 20:32:47",
                "Path": "iot-4e0wsxpi/${device_name}/new-topic-1"
            }
        ],
        "Total": 3
    }
}
```

