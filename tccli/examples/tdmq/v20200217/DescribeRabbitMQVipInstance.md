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
        "ClusterInfo": {
            "ClusterId": "amqp-dsadasd",
            "ClusterName": "abc",
            "Region": "ap-guangzhou",
            "CreateTime": 1,
            "Remark": "abc",
            "Vpcs": [
                {
                    "VpcId": "abc",
                    "SubnetId": "abc",
                    "VpcEndpoint": "abc",
                    "VpcDataStreamEndpointStatus": "1"
                }
            ],
            "ZoneIds": [
                100001
            ],
            "VirtualHostNumber": 10,
            "QueueNumber": 10,
            "MessagePublishRate": 10.1,
            "MessageStackNumber": 10,
            "ExpireTime": 20,
            "ChannelNumber": 10,
            "ConnectionNumber": 10,
            "ConsumerNumber": 10,
            "ExchangeNumber": 10,
            "ExceptionInformation": "abc",
            "ClusterStatus": 1,
            "AutoRenewFlag": 1,
            "MirrorQueuePolicyFlag": 1
        },
        "ClusterSpecInfo": {
            "SpecName": "标准版",
            "NodeCount": 1,
            "MaxTps": 1,
            "MaxBandWidth": 3,
            "MaxStorage": 200,
            "PublicNetworkTps": 1
        },
        "ClusterNetInfo": {
            "PublicAccessEndpoint": "1.1.1.1",
            "WebConsoleEndpoint": "1.1.1.1",
            "WebConsoleUsername": "abc",
            "WebConsolePassword": "abc",
            "PublicAccessEndpointStatus": true,
            "PublicControlConsoleSwitchStatus": true,
            "VpcControlConsoleSwitchStatus": true,
            "VpcWebConsoleEndpoint": "1.1.1.1",
            "PublicWebConsoleSwitchStatus": "ON",
            "VpcWebConsoleSwitchStatus": "ON",
            "PublicDataStreamStatus": "ON",
            "PrometheusEndpointInfo": {
                "PrometheusEndpointStatus": "ON",
                "VpcPrometheusEndpoint": [
                    "abc"
                ],
                "NodePrometheusAddress": [
                    "abc"
                ],
                "VpcEndpointInfo": {
                    "VpcId": "abc",
                    "SubnetId": "abc",
                    "VpcEndpoint": "abc",
                    "VpcDataStreamEndpointStatus": "abc"
                }
            }
        },
        "ClusterWhiteListInfo": {
            "WhiteList": "1.1.1.1",
            "PublicControlConsoleWhiteList": "1.1.1.1",
            "PublicDataStreamWhiteList": "1.1.1.1",
            "PublicControlConsoleWhiteListStatus": "ON",
            "PublicDataStreamWhiteListStatus": "ON"
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
        },
        "RequestId": "abc"
    }
}
```

