**Example 1: 获取单个Amqp集群信息**

-

Input: 

```
tccli tdmq DescribeRabbitMQVipInstance --cli-unfold-argument  \
    --ClusterId amqp-test
```

Output: 
```
{
    "Response": {
        "ClusterInfo": {
            "AutoRenewFlag": 1,
            "ChannelNumber": 1,
            "ClusterId": "amqp-test",
            "ClusterName": "test",
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
                    "SubnetId": "subnet-test1",
                    "VpcDataStreamEndpointStatus": "ON",
                    "VpcEndpoint": "amqp://10.0.0.4:5672",
                    "VpcId": "vpc-test1"
                },
                {
                    "SubnetId": "subnet-test2",
                    "VpcDataStreamEndpointStatus": "ON",
                    "VpcEndpoint": "amqp://10.0.0.10:5672",
                    "VpcId": "vpc-test2"
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
            "PublicAccessEndpoint": "amqp://106.55.176.111:5672",
            "PublicAccessEndpointStatus": true,
            "PublicControlConsoleSwitchStatus": true,
            "PublicDataStreamStatus": "ON",
            "PublicWebConsoleSwitchStatus": "ON",
            "VpcControlConsoleSwitchStatus": false,
            "VpcWebConsoleEndpoint": "http://127.0.0.1:15672",
            "VpcWebConsoleSwitchStatus": "OFF",
            "WebConsoleDomainEndpoint": "http://amqp-test.dashboard.rabbitmq.xx.public.tencenttdmq.com:15672",
            "WebConsoleEndpoint": "http://106.55.176.11:15672",
            "WebConsolePassword": "Fs98DBo9C1IuN4L0",
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
            "PublicControlConsoleWhiteList": "127.0.0.1,171.216.138.56",
            "PublicControlConsoleWhiteListStatus": "ON",
            "PublicDataStreamWhiteList": "127.0.0.1,125.69.38.199",
            "PublicDataStreamWhiteListStatus": "ON",
            "WhiteList": "127.0.0.1,171.216.138.56"
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

