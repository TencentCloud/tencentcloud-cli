**Example 1: 新增Topic**

新增Topic

Input: 

```
tccli iot AddTopic --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --TopicName new-topic-1
```

Output: 
```
{
    "Response": {
        "RequestId": "e2d52ec2-163f-4d53-ab0f-075a4f123073",
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

