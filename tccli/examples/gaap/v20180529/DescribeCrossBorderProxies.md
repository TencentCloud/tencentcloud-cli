**Example 1: 查询通道实例列表**



Input: 

```
tccli gaap DescribeCrossBorderProxies --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name AccessRegion \
    --Filters.0.Values ap-hongkong
```

Output: 
```
{
    "Response": {
        "RequestId": "ca705529-e783-42a3-88c1-2cbe1e915ee6"
    }
}
```

