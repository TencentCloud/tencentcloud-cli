**Example 1: 创建数据库代理**

主实例创建数据库代理

Input: 

```
tccli cdb CreateCdbProxy --cli-unfold-argument  \
    --InstanceId cdb-aykuksx3 \
    --UniqVpcId vpc-ixw3ll2d \
    --UniqSubnetId subnet-0z3r56vq \
    --Desc test \
    --ProxyNodeCustom.0.NodeCount 2 \
    --ProxyNodeCustom.0.Region ap-guangzhou \
    --ProxyNodeCustom.0.Zone ap-guangzhou-1 \
    --ProxyNodeCustom.0.Cpu 1 \
    --ProxyNodeCustom.0.Mem 1
```

Output: 
```
{
    "Response": {
        "RequestId": "123-123",
        "AsyncRequestId": "123-123-123"
    }
}
```

