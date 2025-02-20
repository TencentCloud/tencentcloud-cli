**Example 1: 实例详情示例**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessInstance --cli-unfold-argument  \
    --InstanceId amqp-slnatby
```

Output: 
```
{
    "Response": {
        "RequestId": "bae00352-45fb-46ea-8960-2c8ce102db5f",
        "ClusterInfo": {
            "InstanceType": 1,
            "ClusterName": "devCluster",
            "ClusterId": "amqp-slnatby",
            "Region": "ap-guangzhou",
            "CreateTime": 1737775135000,
            "Remark": "",
            "Vpcs": [
                {
                    "VpcId": "vpc-test",
                    "SubnetId": "subnet-test",
                    "VpcEndpoint": "amqp://10.0.0.1:5672",
                    "VpcDataStreamEndpointStatus": "ON"
                }
            ],
            "ZoneIds": null,
            "VirtualHostNumber": 2,
            "QueueNumber": 11,
            "ChannelNumber": 0,
            "ConnectionNumber": 0,
            "ConsumerNumber": 0,
            "ExchangeNumber": 13,
            "MessagePublishRate": 0,
            "MessageConsumeRate": 0,
            "MessageStackNumber": 19,
            "ExpireTime": 1740453535000,
            "ExceptionInformation": null,
            "ClusterStatus": 1,
            "AutoRenewFlag": 1,
            "ClusterVersion": "0.1.0",
            "PayMode": 0,
            "MessageRetainTime": 72,
            "MirrorQueuePolicyFlag": null
        },
        "ClusterNetInfo": {
            "PublicDataStreamStatus": "OFF",
            "PublicAccessEndpoint": null
        },
        "ClusterWhiteListInfo": {
            "PublicDataStreamWhiteList": null,
            "PublicDataStreamWhiteListStatus": "OFF"
        },
        "ClusterSpecInfo": {
            "SpecName": "BASIC",
            "MaxTps": 2000,
            "MaxQueueNum": 100,
            "MaxVhostNum": 250,
            "MaxExchangeNum": 100,
            "MaxConnNum": 2000,
            "MaxUserNum": 20,
            "MaxBandWidth": 0,
            "PublicNetworkTps": 3
        },
        "VirtualHostQuota": {
            "MaxVirtualHost": 250,
            "UsedVirtualHost": 2
        },
        "ExchangeQuota": {
            "MaxExchange": 100,
            "UsedExchange": 13
        },
        "QueueQuota": {
            "MaxQueue": 100,
            "UsedQueue": 11
        },
        "UserQuota": {
            "MaxUser": 20,
            "UsedUser": 1
        }
    }
}
```

