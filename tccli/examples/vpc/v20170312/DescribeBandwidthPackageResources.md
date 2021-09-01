**Example 1: 查询共享带宽包内的资源列表**



Input: 

```
tccli vpc DescribeBandwidthPackageResources --cli-unfold-argument  \
    --BandwidthPackageId bwp-7umnal1o
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ResourceSet": [
            {
                "ResourceType": "Address",
                "ResourceId": "eip-60z7i46d",
                "AddressIp": "139.199.XX.XX"
            },
            {
                "ResourceType": "Address",
                "ResourceId": "eip-d97psd1o",
                "AddressIp": "139.198.XX.XX"
            }
        ],
        "RequestId": "ecaa7a90-a2fd-4fa3-8bf8-7d0723c95a99"
    }
}
```

