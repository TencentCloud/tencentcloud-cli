**Example 1: 查询共享带宽包内的资源列表**



Input: 

```
tccli vpc DescribeBandwidthPackageResources --cli-unfold-argument  \
    --BandwidthPackageId bwp-9u4iag5l \
    --Filters.0.Name resource-type \
    --Filters.0.Values Address
```

Output: 
```
{
    "Response": {
        "RequestId": "d3093d68-3daf-415c-af74-b5a6b3a383d0",
        "ResourceSet": [
            {
                "AddressIp": "2402:4e00:c000:700:34ee:5b66:3676:d",
                "ResourceId": "eipv6-qqc8i9s7",
                "ResourceType": "Address"
            },
            {
                "AddressIp": "2402:4e00:c000:700:34ee:5b66:3676:8",
                "ResourceId": "eipv6-6ckprob3",
                "ResourceType": "Address"
            }
        ],
        "TotalCount": 2
    }
}
```

