**Example 1: 用于更新vpc内的服务的Route信息的权重**



Input: 

```
tccli vpc UpdateRouteWeightInternal --cli-unfold-argument  \
    --RouteWeightRequestSet.0.VpcId 1 \
    --RouteWeightRequestSet.0.UniqueVpcId vpc-jmaywf6r \
    --RouteWeightRequestSet.0.GroupId 1 \
    --RouteWeightRequestSet.0.Protocol tcp \
    --RouteWeightRequestSet.0.Vip 172.16.0.18 \
    --RouteWeightRequestSet.0.VirtualPort 22 \
    --RouteWeightRequestSet.0.RouteSet.0.PrivateIp 10.19.0.121 \
    --RouteWeightRequestSet.0.RouteSet.0.ProtocolPort 8080 \
    --RouteWeightRequestSet.0.RouteSet.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

