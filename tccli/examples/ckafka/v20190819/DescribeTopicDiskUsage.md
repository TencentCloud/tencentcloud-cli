**Example 1: DescribeTopicDiskUsage**

获取磁盘占用量接口

Input: 

```
tccli ckafka DescribeTopicDiskUsage --cli-unfold-argument  \
    --InstanceId ckafka-xxxasa \
    --TopicName topicNamed
```

Output: 
```
{
    "Response": {
        "RequestId": "cxxxx",
        "Result": {
            "TopicName": "TopicNameds",
            "TopicId": "topic-42n12uin4it",
            "DiskUsage": 10239055
        }
    }
}
```

