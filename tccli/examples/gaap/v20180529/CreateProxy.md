**Example 1: 创建通道2**



Input: 

```
tccli gaap CreateProxy --cli-unfold-argument  \
    --ProjectId 0 \
    --ProxyName proxy-name \
    --AccessRegion Hongkong \
    --Bandwidth 10 \
    --Concurrent 2 \
    --RealServerRegion Shanghai \
    --BillingType 1 \
    --IPAddressVersion IPv4 \
    --NetworkType normal \
    --PackageType Thunder \
    --Http3Supported 0
```

Output: 
```
{
    "Response": {
        "RequestId": "db2dd9d4-ba60-48a2-a9ed-cd18c6e58dd0",
        "InstanceId": "link-nphqtout"
    }
}
```

