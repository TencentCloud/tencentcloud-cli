**Example 1: 查询外网服务**



Input: 

```
tccli vpc DescribeWanServiceInternal --cli-unfold-argument  \
    --VpcId 1 \
    --Protocol tcp \
    --Vip 10.6.2.3 \
    --VirtualPort 8181 \
    --UniqueVpcId vpc-jmaywf6r \
    --Type 1 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "GetWanServiceResult": [
            {
                "VpcId": 1,
                "UniqueVpcId": "vpc-5k6fot41",
                "Protocol": "tcp",
                "VpcGatewayIp": "9.30.232.100",
                "GroupId": [
                    0
                ],
                "Vip": "10.133.192.110",
                "VirtualPort": 81,
                "Type": 1,
                "CreateTime": "2022-06-29 16:54:19"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

