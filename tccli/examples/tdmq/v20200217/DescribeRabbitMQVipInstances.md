**Example 1: 获取实例列表**



Input: 

```
tccli tdmq DescribeRabbitMQVipInstances --cli-unfold-argument  \
    --Filters.0.Name instanceName \
    --Filters.0.Values test \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AutoRenewFlag": 1,
                "ClusterStatus": 1,
                "ConfigDisplay": "体验型",
                "CreateTime": 1730294244007,
                "ExceptionInformation": null,
                "ExpireTime": 1732972644007,
                "InstanceId": "amqp-test",
                "InstanceName": "test1030",
                "InstanceVersion": "3.11.8",
                "MaxBandWidth": 45,
                "MaxStorage": 600,
                "MaxTps": 2400,
                "NodeCount": 3,
                "PayMode": 1,
                "PublicAccessEndpoint": "amqp://106.55.176.111:5672",
                "Remark": "",
                "SpecName": "rabbit-vip-basic-5",
                "Status": 1,
                "Vpcs": [
                    {
                        "SubnetId": "subnet-test",
                        "VpcDataStreamEndpointStatus": "ON",
                        "VpcEndpoint": "amqp://10.0.4.10:5672",
                        "VpcId": "vpc-test"
                    }
                ]
            }
        ],
        "RequestId": "db5e4d5f-e2c5-4a17-9fbd-484ec2d98324",
        "TotalCount": 16
    }
}
```

