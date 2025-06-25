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
    --ProxyNodeCustom.0.Cpu 2 \
    --ProxyNodeCustom.0.Mem 4000
```

Output: 
```
{
    "Response": {
        "RequestId": "3689c0eb-a92d-77ce-0ee2-17d99f604e64",
        "AsyncRequestId": "a6040589-3b098df5-b551d9e5-81c6bfdc"
    }
}
```

