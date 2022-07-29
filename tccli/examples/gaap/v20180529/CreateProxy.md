**Example 1: 创建通道**



Input: 

```
tccli gaap CreateProxy --cli-unfold-argument  \
    --AccessRegion SouthChina \
    --ProjectId 0 \
    --Concurrent 2 \
    --Bandwidth 10 \
    --ProxyName test \
    --GroupId lg-xxxx
```

Output: 
```
{
    "Response": {
        "InstanceId": "link-11112222",
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

**Example 2: 创建通道2**



Input: 

```
tccli gaap CreateProxy --cli-unfold-argument  \
    --Http3Supported 0 \
    --BillingType 0 \
    --AccessRegion Shanghai \
    --Concurrent 2 \
    --ProjectId 0 \
    --RealServerRegion Guangzho \
    --ProxyName test \
    --Bandwidth 10 \
    --PackageType Thunder \
    --NetworkType normal \
    --IPAddressVersion IPv4
```

Output: 
```
{
    "Response": {
        "RequestId": "db2dd9d4-ba60-48a2-a9ed-cd18c6e58dd0",
        "InstanceId": "link-aogd6x07"
    }
}
```

