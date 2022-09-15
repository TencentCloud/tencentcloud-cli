**Example 1: 删除ServiceIPv6**



Input: 

```
tccli vpc DeleteServiceIpv6Internal --cli-unfold-argument  \
    --DelServiceIpv6Set.0.VpcId 1 \
    --DelServiceIpv6Set.0.Protocol tcp \
    --DelServiceIpv6Set.0.Route.0.Weight 1 \
    --DelServiceIpv6Set.0.Route.0.RemoteVpcId 1 \
    --DelServiceIpv6Set.0.Route.0.ZoneId 100002 \
    --DelServiceIpv6Set.0.Route.0.HostIp 1.1.1.1 \
    --DelServiceIpv6Set.0.Route.0.ProtocolPort 80 \
    --DelServiceIpv6Set.0.Route.0.PrivateIp 1.1.1.1 \
    --DelServiceIpv6Set.0.RstFlag 1 \
    --DelServiceIpv6Set.0.DeleteRouteFlag True \
    --DelServiceIpv6Set.0.Vip 10.6.2.3 \
    --DelServiceIpv6Set.0.VirtualPort 80 \
    --DelServiceIpv6Set.0.StickyMaxCount 100 \
    --DelServiceIpv6Set.0.UniqueVpcId vpc-asdasd \
    --DelServiceIpv6Set.0.StickyFlag 1 \
    --DelServiceIpv6Set.0.StickyTimeout 30
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

