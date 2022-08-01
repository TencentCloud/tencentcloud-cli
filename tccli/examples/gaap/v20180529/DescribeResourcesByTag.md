**Example 1: 根据标签拉取资源列表**



Input: 

```
tccli gaap DescribeResourcesByTag --cli-unfold-argument  \
    --ResourceType Proxy \
    --TagKey testkey \
    --TagValue test
```

Output: 
```
{
    "Response": {
        "ResourceSet": [
            {
                "ResourceType": "Proxy",
                "ResourceId": "link-12345678"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

