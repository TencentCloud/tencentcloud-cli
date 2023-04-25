**Example 1: 添加外网服务**

添加外网服务.

Input: 

```
tccli vpc CreateWanServiceInternal --cli-unfold-argument  \
    --AddWanServiceSet.0.Vip 10.6.2.3 \
    --AddWanServiceSet.0.VpcId 1 \
    --AddWanServiceSet.0.Protocol tcp \
    --AddWanServiceSet.0.GroupId 1 \
    --AddWanServiceSet.0.VirtualPort 8181
```

Output: 
```
{
    "Response": {
        "AddWanServiceResult": [
            {
                "Vip": "10.133.192.110",
                "VpcId": 1,
                "UniqueVpcId": "vpc-5k6fot41",
                "Protocol": "tcp",
                "VirtualPort": 81,
                "VpcGatewayIp": "9.30.232.100",
                "Type": 1,
                "CreateTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

