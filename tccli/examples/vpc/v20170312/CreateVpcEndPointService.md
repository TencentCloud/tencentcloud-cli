**Example 1: 创建终端节点服务**

创建终端节点服务

Input: 

```
tccli vpc CreateVpcEndPointService --cli-unfold-argument  \
    --AutoAcceptFlag True \
    --EndPointServiceName 测试 \
    --VpcId vpc-hj3he929 \
    --IsPassService True \
    --ServiceInstanceId lb-nswq8wkq \
    --ServiceType CLB
```

Output: 
```
{
    "Response": {
        "RequestId": "b237f475-49b3-4b10-af8e-071e0a5c7d7a",
        "EndPointService": {
            "VpcId": "vpc-hj3he929",
            "AutoAcceptFlag": "false",
            "ServiceInstanceId": "lb-nswq8wkq",
            "ServiceName": "test_002",
            "EndPointServiceId": "vpcsvc-kngiybxl",
            "ServiceVip": "10.101.1.11",
            "CreateTime": "0000-00-00 00:00:00",
            "ServiceOwner": "1254277469",
            "EndPointCount": 1,
            "EndPointSet": [],
            "ServiceType": "CLB"
        }
    }
}
```

