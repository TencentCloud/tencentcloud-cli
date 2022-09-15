**Example 1: 添加ServiceIPv6**



Input: 

```
tccli vpc CreateServiceIpv6Internal --cli-unfold-argument  \
    --AddServiceIpv6Set.0.VpcId 1 \
    --AddServiceIpv6Set.0.Protocol tcp \
    --AddServiceIpv6Set.0.Route.0.Weight 1 \
    --AddServiceIpv6Set.0.Route.0.RemoteVpcId 1 \
    --AddServiceIpv6Set.0.Route.0.ZoneId 100002 \
    --AddServiceIpv6Set.0.Route.0.HostIp 1.1.1.1 \
    --AddServiceIpv6Set.0.Route.0.ProtocolPort 80 \
    --AddServiceIpv6Set.0.Route.0.PrivateIp 1.1.1.1 \
    --AddServiceIpv6Set.0.RstFlag 1 \
    --AddServiceIpv6Set.0.Vip 10.6.2.3 \
    --AddServiceIpv6Set.0.VirtualPort 80 \
    --AddServiceIpv6Set.0.StickyMaxCount 100 \
    --AddServiceIpv6Set.0.UniqueVpcId vpc-asdasd \
    --AddServiceIpv6Set.0.StickyFlag 1 \
    --AddServiceIpv6Set.0.StickyTimeout 30
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

