**Example 1: 创建通道**



Input: 

```
tccli gaap CreateProxy --cli-unfold-argument  \
    --ProjectId 0 \
    --ProxyName test \
    --AccessRegion SouthChina \
    --Bandwidth 10 \
    --Concurrent 2 \
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

