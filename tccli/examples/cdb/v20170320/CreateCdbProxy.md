**Example 1: 创建数据库代理**

主实例创建数据库代理

Input: 

```
tccli cdb CreateCdbProxy --cli-unfold-argument  \
    --InstanceId cdb-aykuksx3 \
    --UniqVpcId vpc-ixw3ll2d \
    --UniqSubnetId subnet-0z3r56vq \
    --Desc andy_proxy \
    --ProxyNodeCustom.0.NodeCount 2 \
    --ProxyNodeCustom.0.Region ap-guangzhou \
    --ProxyNodeCustom.0.Zone ap-guangzhou-1 \
    --ProxyNodeCustom.0.Cpu 1 \
    --ProxyNodeCustom.0.Mem 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "7EF78BEC-0111-43AF-BB11-111112FB54A7"
    }
}
```

