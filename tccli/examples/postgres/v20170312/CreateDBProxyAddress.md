**Example 1: 创建Proxy连接地址**



Input: 

```
tccli postgres CreateDBProxyAddress --cli-unfold-argument  \
    --DBInstanceId postgres-2wvpv38j \
    --VpcId vpc-1dq8ehm3 \
    --SubnetId subnet-6yui3ok8 \
    --ProxyGroupId proxy-nlpsb4jp \
    --SecurityGroup sg-9rlup3c5 \
    --Description create new address \
    --ConnectionPool True \
    --WeightMode custom \
    --ProxyAllocation.0.NodeId postgres-2wvpv38j \
    --ProxyAllocation.0.Role master \
    --ProxyAllocation.0.Weight 100 \
    --ProxyAllocation.0.Status online \
    --RoAutoAdd True \
    --LatencyRemove True \
    --LatencyRemoveTime 10 \
    --MinRouteNum 1
```

Output: 
```
{
    "Response": {
        "TaskId": 100200,
        "RequestId": "d55c34b5-dfe0-43bf-96e8-df7880f9bace"
    }
}
```

