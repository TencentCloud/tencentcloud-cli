**Example 1: 获取实例列表**



Input: 

```
tccli trabbit ListRabbitMQServerlessInstances --cli-unfold-argument  \
    --Limit 2 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AutoRenewFlag": 1,
                "ClusterStatus": 1,
                "CreateTime": 1737028115000,
                "ExceptionInformation": null,
                "ExpireTime": 1739706515000,
                "InstanceId": "amqp-slfxemauoa",
                "InstanceName": "test_yunchao_8816",
                "InstanceType": 1,
                "InstanceVersion": "0.1.0",
                "MaxBandWidth": 0,
                "MaxStorage": 0,
                "MaxTps": 2000,
                "NodeCount": 0,
                "PayMode": 0,
                "PublicAccessEndpoint": null,
                "Remark": "",
                "SpecName": "基础版",
                "Status": 1,
                "Vpcs": []
            },
            {
                "AutoRenewFlag": 1,
                "ClusterStatus": 1,
                "CreateTime": 1736912606000,
                "ExceptionInformation": null,
                "ExpireTime": 1739591006000,
                "InstanceId": "amqp-slirnlmwlm",
                "InstanceName": "test_yunchao_001",
                "InstanceType": 1,
                "InstanceVersion": "0.1.0",
                "MaxBandWidth": 0,
                "MaxStorage": 0,
                "MaxTps": 2000,
                "NodeCount": 0,
                "PayMode": 0,
                "PublicAccessEndpoint": null,
                "Remark": "",
                "SpecName": "基础版",
                "Status": 1,
                "Vpcs": [
                    {
                        "SubnetId": "subnet-1j1p6omq",
                        "VpcDataStreamEndpointStatus": "ON",
                        "VpcEndpoint": "amqp://10.0.0.2:5672",
                        "VpcId": "vpc-f7zemc2v"
                    }
                ]
            }
        ],
        "RequestId": "cc77d367-76b7-4aef-b5d6-e471ed254758",
        "TotalCount": 4
    }
}
```

