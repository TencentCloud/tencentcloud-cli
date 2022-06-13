**Example 1: 用于删除vpc内的服务的Route信息**



Input: 

```
tccli vpc DeleteRouteInternal --cli-unfold-argument  \
    --RouteInfoRequestSet.0.VpcId 1 \
    --RouteInfoRequestSet.0.UniqueVpcId vpc-jmaywf6r \
    --RouteInfoRequestSet.0.GroupId 0 \
    --RouteInfoRequestSet.0.Type 0 \
    --RouteInfoRequestSet.0.Protocol tcp \
    --RouteInfoRequestSet.0.VirtualPort 22 \
    --RouteInfoRequestSet.0.Vip 172.16.0.18 \
    --RouteInfoRequestSet.0.RouteSet.0.PrivateIp 10.19.0.121 \
    --RouteInfoRequestSet.0.RouteSet.0.ProtocolPort 8080 \
    --RouteInfoRequestSet.0.RouteSet.0.Weight 10 \
    --RouteInfoRequestSet.0.RouteSet.0.ZoneId 1 \
    --RouteInfoRequestSet.0.RouteSet.0.UdpOption 1 \
    --RouteInfoRequestSet.0.RouteSet.0.HostIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

