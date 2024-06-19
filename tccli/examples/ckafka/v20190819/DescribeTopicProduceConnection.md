**Example 1: 获取topic连接信息**

获取topic连接信息

Input: 

```
tccli ckafka DescribeTopicProduceConnection --cli-unfold-argument  \
    --InstanceId ckafka-xxxx \
    --TopicName xxxx
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "IpAddr": "abc",
                "Time": "abc",
                "IsUnSupportVersion": true
            }
        ],
        "RequestId": "abc"
    }
}
```

