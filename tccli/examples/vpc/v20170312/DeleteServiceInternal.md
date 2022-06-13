**Example 1: 用于删除vpc内的服务**



Input: 

```
tccli vpc DeleteServiceInternal --cli-unfold-argument  \
    --ServiceRequestSet.0.VpcId 1 \
    --ServiceRequestSet.0.UniqueVpcId vpc-jmaywf6r \
    --ServiceRequestSet.0.Type 0 \
    --ServiceRequestSet.0.Protocol tcp \
    --ServiceRequestSet.0.VirtualPort 22 \
    --ServiceRequestSet.0.Vip 172.16.0.18 \
    --ServiceRequestSet.0.RemoteVpcId 1 \
    --ServiceRequestSet.0.DeleteRouteFlag 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

