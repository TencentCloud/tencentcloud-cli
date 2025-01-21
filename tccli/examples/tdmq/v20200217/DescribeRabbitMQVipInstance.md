**Example 1: 获取单个Amqp集群信息**

-

Input: 

```
tccli tdmq DescribeRabbitMQVipInstance --cli-unfold-argument  \
    --ClusterId amqp-jero744g
```

Output: 
```
{
    "Response": {
        "ClusterInfo": {
            "AutoRenewFlag": 1,
            "ChannelNumber": 1,
            "ClusterId": "amqp-jero744g",
            "ClusterName": "tencent_cloud",
            "ClusterStatus": 1,
            "ClusterVersion": "3.8.30",
            "ConnectionNumber": 1,
            "ConsumerNumber": 1,
            "CreateTime": 1728982428000,
            "ExceptionInformation": null,
            "ExchangeNumber": 10,
            "ExpireTime": 1731660828257,
            "MessageConsumeRate": 0,
            "MessagePublishRate": 0,
            "MessageStackNumber": 3021165,
            "MirrorQueuePolicyFlag": 1,
            "PayMode": 1,
            "QueueNumber": 1112,
            "Region": "ap-qingyuan",
            "Remark": "",
            "VirtualHostNumber": 1,
            "Vpcs": [
                {
                    "SubnetId": "subnet-67y9wil4",
                    "VpcDataStreamEndpointStatus": "ON",
                    "VpcEndpoint": "amqp://10.0.0.2:5672",
                    "VpcId": "vpc-5ghsr4p9"
                }
            ],
            "ZoneIds": [
                540001
            ]
        },
        "ClusterNetInfo": {
            "PrometheusEndpointInfo": {
                "NodePrometheusAddress": [],
                "PrometheusEndpointStatus": "OFF",
                "VpcEndpointInfo": null,
                "VpcPrometheusEndpoint": []
            },
            "PublicAccessEndpoint": "amqp://127.0.0.1:5672",
            "PublicAccessEndpointStatus": true,
            "PublicControlConsoleSwitchStatus": true,
            "PublicDataStreamStatus": "ON",
            "PublicWebConsoleSwitchStatus": "ON",
            "VpcControlConsoleSwitchStatus": false,
            "VpcWebConsoleEndpoint": "http://127.0.0.1:15672",
            "VpcWebConsoleSwitchStatus": "OFF",
            "WebConsoleDomainEndpoint": "http://amqp-jero744g.dashboard.rabbitmq.xx.public.tencenttdmq.com:15672",
            "WebConsoleEndpoint": "http://127.0.0.1:15672",
            "WebConsolePassword": "Fs78DBo2C3IuN4L0",
            "WebConsoleUsername": "admin"
        },
        "ClusterSpecInfo": {
            "MaxBandWidth": 15,
            "MaxStorage": 200,
            "MaxTps": 800,
            "NodeCount": 1,
            "PublicNetworkTps": 5,
            "SpecName": "体验型"
        },
        "ClusterWhiteListInfo": {
            "PublicControlConsoleWhiteList": "127.0.0.1",
            "PublicControlConsoleWhiteListStatus": "ON",
            "PublicDataStreamWhiteList": "127.0.0.1",
            "PublicDataStreamWhiteListStatus": "ON",
            "WhiteList": "127.0.0.1"
        },
        "ExchangeQuota": {
            "MaxExchange": 1000,
            "UsedExchange": 10
        },
        "QueueQuota": {
            "MaxQueue": 1000,
            "UsedQueue": 1112
        },
        "RequestId": "2a48bbf4-4675-4984-93d9-8ed0f4dfa598",
        "VirtualHostQuota": {
            "MaxVirtualHost": 20,
            "UsedVirtualHost": 1
        }
    }
}
```

