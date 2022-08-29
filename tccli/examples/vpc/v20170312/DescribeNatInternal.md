**Example 1: 用于获取nat的信息**



Input: 

```
tccli vpc DescribeNatInternal --cli-unfold-argument  \
    --VpcId 123123 \
    --NatType TCB \
    --Limit 100 \
    --Offset 0 \
    --Owner 251198225 \
    --UniqueNatId nat-jmaywf6r
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "NatSet": [
            {
                "WanInLimit": 5242880000,
                "VpcId": 81292,
                "UniqueVpcId": "vpc-7f2w7dl7",
                "LastUpdateConnectionsTime": "2021-03-23 15:56:08",
                "Owner": "251197522",
                "UniqueNatId": "nat-dmdqvype",
                "NatId": 25319,
                "Zone": "ap-guangzhou-2",
                "ZoneId": 100002,
                "State": 1,
                "OwedWanOutLimit": 10485760,
                "NatType": "NAT",
                "GwId": 1,
                "HealthStatus": 0,
                "DetectGwIp": "9.115.33.170",
                "GatewayIp": "9.115.33.170",
                "CreateTime": "2021-03-23 15:56:08",
                "Connections": 1000000,
                "OwedFlag": 0,
                "Name": "new_t_nat",
                "LastMaxConnections": 1000000,
                "GwType": 1,
                "WanOutLimit": 10485760
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

