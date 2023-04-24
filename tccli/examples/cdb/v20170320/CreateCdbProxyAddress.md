**Example 1: 创建数据库代理地址**

创建数据库代理地址

Input: 

```
tccli cdb CreateCdbProxyAddress --cli-unfold-argument  \
    --ProxyGroupId proxy-il2nlsdn \
    --UniqVpcId vpc-ixw3ll2d \
    --UniqSubnetId subnet-0z3r56vq \
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

