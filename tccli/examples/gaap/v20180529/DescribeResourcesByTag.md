**Example 1: Pulling a Resource List Based on Tags**



Input: 

```
tccli gaap DescribeResourcesByTag --cli-unfold-argument  \
    --TagKey testkey \
    --TagValue test \
    --ResourceType Proxy
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

