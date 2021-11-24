**Example 1: 获取amqp集群列表**



Input: 

```
tccli tdmq DescribeAMQPClusters --cli-unfold-argument  \
    --NameKeyword test \
    --IdKeyword amqp-dsadasd \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "ClusterList": [
            {
                "Info": {
                    "Remark": "xx",
                    "PublicEndPoint": "xx",
                    "ClusterName": "xx",
                    "Region": "xx",
                    "ClusterId": "xx",
                    "VpcEndPoint": "xx",
                    "CreateTime": 1
                },
                "Config": {
                    "MaxExchangeNum": 1,
                    "MaxRetentionTime": 1,
                    "UsedVHostNum": 1,
                    "UsedQueueNum": 1,
                    "MaxQueueNum": 1,
                    "MaxConnNumPerVHost": 1,
                    "MaxTpsPerVHost": 1,
                    "MaxVHostNum": 1,
                    "UsedExchangeNum": 1
                }
            }
        ],
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df",
        "TotalCount": 1
    }
}
```

