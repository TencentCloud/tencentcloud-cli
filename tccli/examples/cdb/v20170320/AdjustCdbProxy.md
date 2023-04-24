**Example 1: 调整数据库代理**

调整数据库代理配置

Input: 

```
tccli cdb AdjustCdbProxy --cli-unfold-argument  \
    --InstanceId cdb-aykuksx3 \
    --ProxyGroupId proxy-il2nlsdn \
    --ReloadBalance auto \
    --UpgradeTime nowTime \
    --ProxyNodeCustom.0.NodeCount 2 \
    --ProxyNodeCustom.0.Region ap-guangzhou \
    --ProxyNodeCustom.0.Zone ap-guangzhou-1 \
    --ProxyNodeCustom.0.Cpu 3 \
    --ProxyNodeCustom.0.Mem 4
```

Output: 
```
{
    "Response": {
        "RequestId": "123-123-123",
        "AsyncRequestId": "123-123-xxx"
    }
}
```

