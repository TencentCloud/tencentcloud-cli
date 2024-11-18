**Example 1: 获取可用区配额**

查看可用区内所有机型的配额信息

Input: 

```
tccli cube DescribeZoneInstanceTypeInventory --cli-unfold-argument  \
    --Filters.0.Values ap-chongqing-1 \
    --Filters.0.Name zone
```

Output: 
```
{
    "Response": {
        "InstanceTypeQuotaSet": [
            {
                "Zone": "ap-chongqing-2",
                "Memory": 256,
                "CpuType": "INTEL"
            }
        ],
        "RequestId": "96ac7e0d-778b-4ed3-95a4-e9b355065292"
    }
}
```

