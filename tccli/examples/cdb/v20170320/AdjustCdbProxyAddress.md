**Example 1: 调整数据库代理地址**

调整数据库代理地址

Input: 

```
tccli cdb AdjustCdbProxyAddress --cli-unfold-argument  \
    --ProxyGroupId proxy-il2nlsdn \
    --ProxyAddressId proxy-il2nlsdn \
    --IsKickOut True \
    --MinCount 1 \
    --MaxDelay 10 \
    --WeightMode custom \
    --FailOver True \
    --AutoAddRo True \
    --ReadOnly False \
    --TransSplit False \
    --ConnectionPool True \
    --ProxyAllocation.0.Region ap-guangzhou \
    --ProxyAllocation.0.Zone ap-guangzhou-2 \
    --ProxyAllocation.0.ProxyInstance.0.InstanceId cdb-aykuksx3 \
    --ProxyAllocation.0.ProxyInstance.0.Weight 100
```

Output: 
```
{
    "Response": {
        "RequestId": "111-1314-333-2321212",
        "AsyncRequestId": "test"
    }
}
```

