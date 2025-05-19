**Example 1: TKE集群更新跨租户弹性网卡全局配置**



Input: 

```
tccli tke UpdateMetaFeature --cli-unfold-argument  \
    --TenantParam.UniqVpcId xx \
    --TenantParam.AppId 12345 \
    --TenantParam.Uin xx \
    --TenantParam.SubnetId xx \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "232323-5ed9-4cb7-9194-a95e2cd626e5"
    }
}
```

