**Example 1: 查看消息转发配置详情**



Input: 

```
tccli iotvideoindustry DescribeMessageForward --cli-unfold-argument  \
    --IntId 1
```

Output: 
```
{
    "Response": {
        "CreateTime": "2021-09-30T17:26:47+08:00",
        "Instance": "ckafka",
        "InstanceName": "卡夫卡",
        "IntId": 1,
        "MessageType": "[1]",
        "RegionId": "gz",
        "RegionName": "广州",
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f",
        "TopicId": "topic",
        "Uin": "admin",
        "TopicName": "topicname"
    }
}
```

