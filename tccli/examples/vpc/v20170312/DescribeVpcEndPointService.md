**Example 1: 查询终端节点服务列表**

查询终端节点服务列表

Input: 

```
tccli vpc DescribeVpcEndPointService --cli-unfold-argument  \
    --EndPointServiceIds vpcsvc-kngiybxl \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "EndPointServiceSet": [
            {
                "EndPointServiceId": "vpcsvc-pnpcflil",
                "VpcId": "vpc-hj3he929",
                "ServiceOwner": "1254277469",
                "ServiceName": "test_002",
                "ServiceVip": "10.101.1.11",
                "ServiceInstanceId": "lb-nswq8wkq",
                "AutoAcceptFlag": true,
                "EndPointCount": 1,
                "EndPointSet": [
                    {
                        "ServiceVpcId": "vpc-hj3he929",
                        "GroupSet": [
                            "sg-tyhgrwet"
                        ],
                        "ServiceName": "测试",
                        "State": "PENDING",
                        "ServiceVip": "10.101.1.11",
                        "EndPointName": "节点",
                        "VpcId": "vpc-hj3he929",
                        "EndPointOwner": "1302384414",
                        "EndPointId": "vpce-h0fk8lfc",
                        "SubnetId": "subnet-4t7fr3fi",
                        "CreateTime": "0000-00-00 00:00:00",
                        "EndPointServiceId": "vpcsvc-kngiybxl",
                        "EndPointVip": "10.101.1.11"
                    }
                ],
                "CreateTime": "0000-00-00 00:00:00",
                "ServiceType": "CLB"
            }
        ],
        "TotalCount": 1,
        "RequestId": "452e8b38-10a1-4d8a-8a31-a64b89c8f565"
    }
}
```

