**Example 1: 用于更新vpc内的服务的Route信息**



Input: 

```
tccli vpc UpdateRouteInternal --cli-unfold-argument  \
    --UpdateRouteSet.0.VpcId 1 \
    --UpdateRouteSet.0.Protocol tcp \
    --UpdateRouteSet.0.Update.0.ProtocolPort 80 \
    --UpdateRouteSet.0.Update.0.Weight 16 \
    --UpdateRouteSet.0.Update.0.PrivateIp 1.1.1.1 \
    --UpdateRouteSet.0.Vip 172.16.0.18 \
    --UpdateRouteSet.0.VirtualPort 22 \
    --UpdateRouteSet.0.UniqueVpcId vpc-jmaywf6r \
    --UpdateRouteSet.0.Type 1 \
    --UpdateRouteSet.0.GroupId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

