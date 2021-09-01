**Example 1: 获取Topic信息**

获取Topic信息

Input: 

```
tccli iot GetTopic --cli-unfold-argument  \
    --TopicId topic-7gjao342 \
    --ProductId iot-4e0wsxpi
```

Output: 
```
{
    "Response": {
        "RequestId": "58798947-964f-4982-a3db-f8125ae67b35",
        "Topic": {
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
    }
}
```

