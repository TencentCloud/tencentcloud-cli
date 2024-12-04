**Example 1: 获取topic连接信息**

获取topic连接信息

Input: 

```
tccli ckafka DescribeTopicProduceConnection --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --TopicName topic-name
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "IpAddr": "10.23.1.1",
                "Time": "2020-08-21 11:15:54",
                "IsUnSupportVersion": true
            }
        ],
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

