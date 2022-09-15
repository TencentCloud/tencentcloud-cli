**Example 1: 删除外网服务**



Input: 

```
tccli vpc DeleteWanServiceInternal --cli-unfold-argument  \
    --DelWanServiceSet.0.Vip 10.6.2.3 \
    --DelWanServiceSet.0.VpcId 1 \
    --DelWanServiceSet.0.Protocol tcp \
    --DelWanServiceSet.0.GroupId 1 \
    --DelWanServiceSet.0.VirtualPort 8181
```

Output: 
```
{
    "Response": {
        "DelWanServiceResult": [
            {
                "VpcId": 1,
                "UniqueVpcId": "vpc-5k6fot41",
                "Protocol": "tcp",
                "VpcGatewayIp": "9.30.232.100",
                "CreateTime": "2022-06-29 16:54:19",
                "Vip": "10.133.192.110",
                "VirtualPort": 81,
                "Type": 1
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

