**Example 1: 获取单个Amqp集群信息**

-

Input: 

```
tccli tdmq DescribeRabbitMQVipInstance --cli-unfold-argument  \
    --ClusterId amqp-dsadasd
```

Output: 
```
{
    "Response": {
        "ClusterSpecInfo": {
            "SpecName": "标准版",
            "NodeCount": 1,
            "MaxTps": 1,
            "MaxBandWidth": 1,
            "MaxStorage": 1,
            "PublicNetworkTps": 1
        },
        "ClusterInfo": {
            "Remark": "xx",
            "ClusterName": "xx",
            "Region": "xx",
            "ClusterId": "xx",
            "CreateTime": 1,
            "Vpcs": [
                {
                    "SubnetId": "xx",
                    "VpcId": "xx",
                    "VpcEndpoint": "xx"
                }
            ],
            "ZoneIds": [
                100001
            ],
            "VirtualHostNumber": 10,
            "QueueNumber": 10,
            "MessagePublishRate": 10.1,
            "MessageStackNumber": 10,
            "ExpireTime": 1666257531143
        },
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df",
        "ClusterNetInfo": {
            "WebConsolePassword": "xx",
            "WebConsoleEndpoint": "xx",
            "WebConsoleUsername": "xx",
            "PublicAccessEndpointStatus": true,
            "PublicControlConsoleSwitchStatus": true
        },
        "ClusterWhiteListInfo": {
            "WhiteList": "1.2.3.4,5.6.7.8",
            "PublicControlConsoleWhiteList": "1.2.3.4,5.6.7.8",
            "PublicDataStreamWhiteList": "1.2.3.4,5.6.7.8"
        },
        "VirtualHostQuota": {
            "MaxVirtualHost": 10,
            "UsedVirtualHost": 10
        },
        "ExchangeQuota": {
            "MaxExchange": 10,
            "UsedExchange": 10
        },
        "QueueQuota": {
            "MaxQueue": 10,
            "UsedQueue": 10
        }
    }
}
```

