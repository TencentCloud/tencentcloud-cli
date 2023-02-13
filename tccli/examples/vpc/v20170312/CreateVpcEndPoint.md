**Example 1: 创建终端节点**

创建终端节点

Input: 

```
tccli vpc CreateVpcEndPoint --cli-unfold-argument  \
    --SubnetId subnet-4t7fr3fi \
    --EndPointName point_002 \
    --VpcId vpc-coekkqtd \
    --EndPointServiceId vpcsvc-kngiybxl
```

Output: 
```
{
    "Response": {
        "EndPoint": {
            "ServiceVpcId": "vpc-hj3he929",
            "VpcId": "vpc-coekkqtd",
            "State": "PENDING",
            "ServiceVip": "10.101.1.11",
            "EndPointName": "point_002",
            "GroupSet": [],
            "EndPointOwner": "1302384414",
            "EndPointId": "vpce-h0fk8lfc",
            "SubnetId": "subnet-4t7fr3fi",
            "CreateTime": "0000-00-00 00:00:00",
            "EndPointServiceId": "vpcsvc-kngiybxl",
            "EndPointVip": "10.0.0.8",
            "ServiceName": "服务"
        },
        "RequestId": "fefb383a-7394-46c9-ba34-6b21e8fb3ac1"
    }
}
```

