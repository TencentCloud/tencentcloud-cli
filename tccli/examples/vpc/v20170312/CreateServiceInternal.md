**Example 1: 用于添加vpc内的服务**



Input: 

```
tccli vpc CreateServiceInternal --cli-unfold-argument  \
    --NewServiceSet.0.VpcId 1 \
    --NewServiceSet.0.UniqueVpcId vpc-jmaywf6r \
    --NewServiceSet.0.Type 0 \
    --NewServiceSet.0.Protocol tcp \
    --NewServiceSet.0.VirtualPort 22 \
    --NewServiceSet.0.Vip 172.16.0.18 \
    --NewServiceSet.0.RemoteVpcId 1 \
    --NewServiceSet.0.UniqueVpcGatewayId xxx \
    --NewServiceSet.0.UniqueClassicVpcGatewayId xxx \
    --NewServiceSet.0.VipVpcGatewayId xxx \
    --NewServiceSet.0.VpcGatewayIp 1.1.1.1 \
    --NewServiceSet.0.VpcGatewayType 1 \
    --NewServiceSet.0.VpcGatewayZoneId 1 \
    --NewServiceSet.0.VpcGatewayAttrFlag 0 \
    --NewServiceSet.0.SubnetRouteAlgorithm 0 \
    --NewServiceSet.0.NoSnatFlag 0 \
    --NewServiceSet.0.StickyFlag 0 \
    --NewServiceSet.0.StickyTimeout 0 \
    --NewServiceSet.0.StickyMaxCount 0 \
    --NewServiceSet.0.LbType 0 \
    --NewServiceSet.0.ResetFlag 0 \
    --NewServiceSet.0.BypassFlag 0 \
    --NewServiceSet.0.Business xxx \
    --NewServiceSet.0.RouteGroupFlag 0 \
    --NewServiceSet.0.RouteGroupId 1 \
    --NewServiceSet.0.UniqueRouteGroupId xxx \
    --NewServiceSet.0.RouteSet.0.PrivateIp 10.19.0.121 \
    --NewServiceSet.0.RouteSet.0.ProtocolPort 8080 \
    --NewServiceSet.0.RouteSet.0.Weight 10 \
    --NewServiceSet.0.RouteSet.0.ZoneId 1 \
    --NewServiceSet.0.RouteSet.0.UdpOption 1 \
    --NewServiceSet.0.RouteSet.0.HostIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

