**Example 1: 查看消息转发配置列表**



Input: 

```
tccli iotvideoindustry DescribeMessageForwards --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "IntId": 1,
                "Uin": "admin",
                "MessageType": "[1]",
                "RegionName": "广州",
                "Instance": "ckafka",
                "InstanceName": "卡夫卡",
                "TopicId": "topic",
                "TopicName": "topicname",
                "CreateTime": "2021-09-30T17:26:47+08:00",
                "UpdateTime": "2021-09-30T17:26:47+08:00"
            }
        ],
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f",
        "Total": 1
    }
}
```

