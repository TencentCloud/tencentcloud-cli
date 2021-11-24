**Example 1: 获取单个Amqp集群信息**



Input: 

```
tccli tdmq DescribeAMQPCluster --cli-unfold-argument  \
    --ClusterId amqp-dsadasd
```

Output: 
```
{
    "Response": {
        "ClusterConfig": {
            "MaxExchangeNum": 1,
            "MaxRetentionTime": 1,
            "UsedVHostNum": 1,
            "UsedQueueNum": 1,
            "MaxQueueNum": 1,
            "MaxConnNumPerVHost": 1,
            "MaxTpsPerVHost": 1,
            "MaxVHostNum": 1,
            "UsedExchangeNum": 1
        },
        "ClusterInfo": {
            "Remark": "xx",
            "PublicEndPoint": "xx",
            "ClusterName": "xx",
            "Region": "xx",
            "ClusterId": "xx",
            "VpcEndPoint": "xx",
            "CreateTime": 1
        },
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df",
        "ClusterStats": {
            "ExchangeNum": 1,
            "ProducedMsgNum": 1,
            "AccumulativeMsgNum": 1,
            "QueueNum": 1
        }
    }
}
```

