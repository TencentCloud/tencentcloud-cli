**Example 1: 获取实例Prometheus信息**



Input: 

```
tccli ckafka DescribePrometheus --cli-unfold-argument  \
    --InstanceId ckafka-na37x9qa
```

Output: 
```
{
    "Response": {
        "RequestId": "a49797c5-c350-4de6-b555-321f2bed255b",
        "Result": [
            {
                "BrokerIp": "10.0.137.216",
                "SourceIp": "10.0.1.44",
                "SourcePort": 60001,
                "SubnetId": null,
                "Type": "JmxExport",
                "VpcId": null
            },
            {
                "BrokerIp": "10.0.137.216",
                "SourceIp": "10.0.1.44",
                "SourcePort": 60002,
                "SubnetId": null,
                "Type": "NodeExport",
                "VpcId": null
            },
            {
                "BrokerIp": "10.0.158.67",
                "SourceIp": "10.0.1.44",
                "SourcePort": 60003,
                "SubnetId": null,
                "Type": "JmxExport",
                "VpcId": null
            },
            {
                "BrokerIp": "10.0.158.67",
                "SourceIp": "10.0.1.44",
                "SourcePort": 60004,
                "SubnetId": null,
                "Type": "NodeExport",
                "VpcId": null
            },
            {
                "BrokerIp": "10.0.149.242",
                "SourceIp": "10.0.1.44",
                "SourcePort": 60005,
                "SubnetId": null,
                "Type": "JmxExport",
                "VpcId": null
            },
            {
                "BrokerIp": "10.0.149.242",
                "SourceIp": "10.0.1.44",
                "SourcePort": 60006,
                "SubnetId": null,
                "Type": "NodeExport",
                "VpcId": null
            }
        ]
    }
}
```

