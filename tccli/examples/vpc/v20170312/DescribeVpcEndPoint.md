**Example 1: 查询终端节点列表**

查询终端节点列表

Input: 

```
tccli vpc DescribeVpcEndPoint --cli-unfold-argument  \
    --Limit 1 \
    --EndPointId vpce-h0fk8lfc \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "7e6f5074-e4a2-4bb6-9cac-d2357a00896f",
        "EndPointSet": [
            {
                "ServiceVpcId": "vpc-hj3he929",
                "GroupSet": [
                    "sg-tyhgrwet"
                ],
                "ServiceName": "demo",
                "State": "PENDING",
                "ServiceVip": "10.101.1.11",
                "EndPointName": "demo",
                "VpcId": "vpc-hj3he929",
                "EndPointOwner": "1302384414",
                "EndPointId": "vpce-h0fk8lfc",
                "SubnetId": "subnet-4t7fr3fi",
                "CreateTime": "2022-06-08 10:00:00",
                "EndPointServiceId": "vpcsvc-kngiybxl",
                "EndPointVip": "10.101.1.11"
            }
        ]
    }
}
```

