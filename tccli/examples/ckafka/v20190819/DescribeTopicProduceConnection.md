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
                "IpAddr": "xxxxx",
                "Time": "2021-10-10 21:10:48"
            }
        ],
        "RequestId": "xx"
    }
}
```

