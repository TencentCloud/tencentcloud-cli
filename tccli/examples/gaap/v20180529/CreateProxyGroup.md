**Example 1: 创建通道组**



Input: 

```
tccli gaap CreateProxyGroup --cli-unfold-argument  \
    --ProjectId 0 \
    --GroupName group-name-01 \
    --RealServerRegion Shanghai \
    --AccessRegionSet.0.AccessRegion Guangzhou \
    --AccessRegionSet.0.Bandwidth 10 \
    --AccessRegionSet.0.Concurrent 2 \
    --AccessRegionSet.0.NetworkType normal \
    --IPAddressVersion IPv4 \
    --PackageType Thunder \
    --Http3Supported 0
```

Output: 
```
{
    "Response": {
        "GroupId": "lg-joaaddy1",
        "RequestId": "bf4afc35-3796-40ee-8fad-c1d53745cb66"
    }
}
```

