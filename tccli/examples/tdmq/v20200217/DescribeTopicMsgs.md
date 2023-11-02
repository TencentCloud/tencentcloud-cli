**Example 1: 消息查询**



Input: 

```
tccli tdmq DescribeTopicMsgs --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName test-topic3 \
    --StartTime '2020-09-22 00:00:00' \
    --EndTime '2020-09-22 00:00:00'
```

Output: 
```
{
    "Response": {
        "TotalCount": 10000,
        "TopicMsgLogSets": [
            {
                "MsgId": "15591:9:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:14,281",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:8:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:14,074",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:7:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:13,867",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:6:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:13,658",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:5:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:13,449",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:4:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:13,242",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:3:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:13,015",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:2:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:12,808",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:1:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:12,600",
                "ProducerAddr": "9.139.220.17:37960"
            },
            {
                "MsgId": "15591:0:-1",
                "ProducerName": "fisrtProducer",
                "ProduceTime": "2020-08-14 16:47:12,390",
                "ProducerAddr": "9.139.220.17:37960"
            }
        ],
        "RequestId": "msgs"
    }
}
```

