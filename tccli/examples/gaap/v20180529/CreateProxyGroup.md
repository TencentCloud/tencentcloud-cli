**Example 1: 创建通道组**



Input: 

```
tccli gaap CreateProxyGroup --cli-unfold-argument  \
    --ProjectId 0 \
    --RealServerRegion EastChina \
    --GroupName test
```

Output: 
```
{
    "Response": {
        "RequestId": "19a021f8-dff3-4890-8e7a-ed5054e22e49",
        "GroupId": "lg-negxun2x"
    }
}
```

**Example 2: CreateProxyGroup**



Input: 

```
tccli gaap CreateProxyGroup --cli-unfold-argument  \
    --Http3Supported 0 \
    --ProjectId 0 \
    --RealServerRegion Shanghai \
    --GroupName benny-test \
    --PackageType Thunder \
    --IPAddressVersion IPv4 \
    --AccessRegionSet.0.NetworkType normal \
    --AccessRegionSet.0.Bandwidth 10 \
    --AccessRegionSet.0.AccessRegion Guangzho \
    --AccessRegionSet.0.Concurrent 2
```

Output: 
```
{
    "Response": {
        "RequestId": "1858c87c-2110-430d-bd09-f86091127fe0",
        "GroupId": "lg-cj8rn2up"
    }
}
```

