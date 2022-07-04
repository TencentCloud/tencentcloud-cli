**Example 1: 添加经jnsgw的服务**



Input: 

```
tccli vpc CreateNatGatewayServiceInternal --cli-unfold-argument  \
    --NatServiceRequestSet.0.VpcId 123 \
    --NatServiceRequestSet.0.UniqueVpcId vpc-jmaywf6r \
    --NatServiceRequestSet.0.Owner 251198225 \
    --NatServiceRequestSet.0.Protocol tcp \
    --NatServiceRequestSet.0.PrivateIp 172.16.0.18 \
    --NatServiceRequestSet.0.ProtocolPort 554 \
    --NatServiceRequestSet.0.VirtualGatewayType 0 \
    --NatServiceRequestSet.0.VpcGatewayIndex xxx \
    --NatServiceRequestSet.0.UniqueVpcGatewayIndex xxx \
    --NatServiceRequestSet.0.SubnetId 123 \
    --NatServiceRequestSet.0.Count 10 \
    --NatServiceRequestSet.0.GatewayIp 1.1.1.1 \
    --NatServiceRequestSet.0.VirtualPort 111 \
    --NatServiceRequestSet.0.SkipCheckPrivateIpDatabaseFlag 0 \
    --NatServiceRequestSet.0.Business xxx \
    --NatServiceRequestSet.0.BusinessOwner xxx \
    --NatServiceRequestSet.0.Bandwidth 10
```

Output: 
```
{
    "Response": {
        "NatServiceSet": [
            {
                "VpcId": 78257,
                "UniqueVpcId": "vpc-jmaywf6r",
                "SubnetId": 1990866,
                "Owner": "251198225",
                "Vip": "9.241.203.205",
                "UniqueSubnetId": "subnet-am4aebsm",
                "PrivateIp": "172.16.0.18",
                "GatewayIp": "9.241.203.205",
                "VirtualPort": 13803,
                "Business": "xx",
                "VirtualGatewayType": 0,
                "Protocol": "tcp",
                "ProtocolPort": 554,
                "Bandwidth": 0,
                "CreateTime": "2021-12-27 18:09:40",
                "UniqueVpcGatewayIndex": "172.16.0.18",
                "VpcGatewayIndex": "172.16.0.18",
                "PoolId": 33362,
                "BusinessOwner": "xx"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

