**Example 1: 修改读写分离参数**



Input: 

```
tccli postgres ModifyDBProxyAddress --cli-unfold-argument  \
    --DBInstanceId postgres-2wvpv38j \
    --AddressId proxyaddr-hw78kg1m \
    --ProxyGroupId proxy-nlpsb4jp \
    --Description modify \
    --ConnectionPool False \
    --WeightMode custom \
    --ProxyAllocation.0.NodeId postgres-2wvpv38j \
    --ProxyAllocation.0.Role master \
    --ProxyAllocation.0.Status online \
    --RoAutoAdd False \
    --LatencyRemove False \
    --LatencyRemoveTime 10 \
    --MinRouteNum 1
```

Output: 
```
{
    "Response": {
        "TaskId": 100201,
        "RequestId": "15624379-9192-459e-97f4-52cdc4043a3a"
    }
}
```

