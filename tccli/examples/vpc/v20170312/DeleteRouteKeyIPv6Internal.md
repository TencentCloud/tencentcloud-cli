**Example 1: 用于删除vpc内的服务的Route信息**



Input: 

```
tccli vpc DeleteRouteKeyIPv6Internal --cli-unfold-argument  \
    --DelRouteKeyIPv6Set.0.VpcId 123123 \
    --DelRouteKeyIPv6Set.0.Protocol tcp \
    --DelRouteKeyIPv6Set.0.RemoteVpcId 123 \
    --DelRouteKeyIPv6Set.0.Vip 10.6.2.3 \
    --DelRouteKeyIPv6Set.0.VirtualPort 8181 \
    --DelRouteKeyIPv6Set.0.ProtocolPort 80 \
    --DelRouteKeyIPv6Set.0.UniqueVpcId vpc-jmaywf6r \
    --DelRouteKeyIPv6Set.0.PrivateIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

