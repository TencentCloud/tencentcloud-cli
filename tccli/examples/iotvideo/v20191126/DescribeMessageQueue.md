**Example 1: 获取产品转发消息配置**



Input: 

```
tccli iotvideo DescribeMessageQueue --cli-unfold-argument  \
    --ProductId 12345678910
```

Output: 
```
{
    "Response": {
        "RequestId": "9187436e-0738-4449-ba8e-88882c59c9c9",
        "Data": {
            "MsgQueueType": 2,
            "MsgType": "0,1,2,3,4,5",
            "Topic": "testTopic",
            "Instance": "testInstance",
            "MsgRegion": "xxx"
        }
    }
}
```

