**Example 1: 用于更新vpc内的服务的属性**



Input: 

```
tccli vpc UpdateServicePropertyInternal --cli-unfold-argument  \
    --ServicePropertyRequestSet.0.StickMaxCount 0 \
    --ServicePropertyRequestSet.0.VpcId 1 \
    --ServicePropertyRequestSet.0.Protocol tcp \
    --ServicePropertyRequestSet.0.ToaHostIpFlag 1 \
    --ServicePropertyRequestSet.0.BypassFlag 1 \
    --ServicePropertyRequestSet.0.StickTimeout 1 \
    --ServicePropertyRequestSet.0.StickFlag 0 \
    --ServicePropertyRequestSet.0.LbType 1 \
    --ServicePropertyRequestSet.0.Vip 172.16.0.18 \
    --ServicePropertyRequestSet.0.RouteGroupFlag 1 \
    --ServicePropertyRequestSet.0.RealServerAllDeadAsAliveFlag 1 \
    --ServicePropertyRequestSet.0.VirtualPort 22 \
    --ServicePropertyRequestSet.0.UniqueRouteGroupId xxx \
    --ServicePropertyRequestSet.0.UniqueVpcId vpc-jmaywf6r \
    --ServicePropertyRequestSet.0.RouteGroupId 1 \
    --ServicePropertyRequestSet.0.GroupId 1 \
    --ServicePropertyRequestSet.0.ResetFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

**Example 2: demo**



Input: 

```
tccli vpc UpdateServicePropertyInternal --cli-unfold-argument  \
    --ServicePropertyRequestSet.0.ResetFlag 1 \
    --ServicePropertyRequestSet.0.VpcId 16769060 \
    --ServicePropertyRequestSet.0.Protocol tcp \
    --ServicePropertyRequestSet.0.Vip 172.16.0.18 \
    --ServicePropertyRequestSet.0.VirtualPort 22 \
    --ServicePropertyRequestSet.0.UniqueVpcId vpc-7zayowkt \
    --ServicePropertyRequestSet.0.GroupId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d49ea9de-6ed3-449d-a259-cb8666761470"
    }
}
```

