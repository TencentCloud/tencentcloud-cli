**Example 1: 用于获取终端节点信息**



Input: 

```
tccli vpc DescribeEndPointInternal --cli-unfold-argument  \
    --VpcId 1 \
    --UniqueEndPointServiceId vpcesvc-60gjk01t \
    --SubnetId 123123 \
    --Vip 1.1.1.1 \
    --Limit 100 \
    --Offset 0 \
    --Owner 1231231 \
    --UniqueVpcId vpc-jmaywf6r \
    --EndPointServiceId 1213123
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "GetEndPointResult": [
            {
                "ServiceVpcId": 0,
                "UniqueServiceVpcId": "vpc_0",
                "VpcId": 16769060,
                "Name": "testt",
                "UniqueVpcId": "vpc-7zayowkt",
                "Vip": "10.0.0.4",
                "UniqueEndPointId": "vpce-d2cthiv2",
                "ServiceType": 1,
                "Owner": "251197522",
                "State": 0,
                "IsolateTime": "2022-06-29 14:45:03",
                "UniqueSubnetId": "subnet-1ufvulum",
                "IsolateFlag": 0,
                "EndPointId": 1141,
                "ServiceVip": "10.0.0.17",
                "SubnetId": 2007467,
                "UniqueEndPointServiceId": "",
                "CreateTime": "2022-06-29 14:45:03",
                "EndPointServiceId": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

