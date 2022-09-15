**Example 1: 更新RouteIPv6**



Input: 

```
tccli vpc UpdateRouteIpv6Internal --cli-unfold-argument  \
    --UpdateRouteIpv6Set.0.VpcId 1 \
    --UpdateRouteIpv6Set.0.Protocol tcp \
    --UpdateRouteIpv6Set.0.Update.0.Weight 1 \
    --UpdateRouteIpv6Set.0.Update.0.RemoteVpcId 1 \
    --UpdateRouteIpv6Set.0.Update.0.ZoneId 100002 \
    --UpdateRouteIpv6Set.0.Update.0.HostIp 1.1.1.1 \
    --UpdateRouteIpv6Set.0.Update.0.ProtocolPort 80 \
    --UpdateRouteIpv6Set.0.Update.0.PrivateIp 1.1.1.1 \
    --UpdateRouteIpv6Set.0.Vip 10.6.2.3 \
    --UpdateRouteIpv6Set.0.VirtualPort 80 \
    --UpdateRouteIpv6Set.0.UniqueVpcId vpc-asdasd
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

