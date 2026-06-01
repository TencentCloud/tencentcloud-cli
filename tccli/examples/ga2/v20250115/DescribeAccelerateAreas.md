**Example 1: 查询加速地域**



Input: 

```
tccli ga2 DescribeAccelerateAreas --cli-unfold-argument  \
    --GlobalAcceleratorId ga-ibay3qzs
```

Output: 
```
{
    "Response": {
        "AccelerateAreaSet": [
            {
                "AccelerateRegion": "ap-beijing",
                "AcceleratorAreaId": "area-03ylr758",
                "Bandwidth": 100,
                "IpAddress": [
                    "43.144.128.212"
                ],
                "IpVersion": "IPv4",
                "IspType": "BGP"
            },
            {
                "AccelerateRegion": "ap-shanghai",
                "AcceleratorAreaId": "area-4axcep7u",
                "Bandwidth": 50,
                "IpAddress": [
                    "49.234.245.60"
                ],
                "IpVersion": "IPv4",
                "IspType": "BGP"
            },
            {
                "AccelerateRegion": "ap-hongkong",
                "AcceleratorAreaId": "area-9ocqek4k",
                "Bandwidth": 200,
                "IpAddress": [
                    "129.226.79.200"
                ],
                "IpVersion": "IPv4",
                "IspType": "BGP"
            },
            {
                "AccelerateRegion": "ap-guangzhou",
                "AcceleratorAreaId": "area-n5gb14ck",
                "Bandwidth": 1,
                "IpAddress": [
                    "81.71.246.171"
                ],
                "IpVersion": "IPv4",
                "IspType": "BGP"
            }
        ],
        "RequestId": "14bd9eb8-8e53-4c12-942a-186666d4811f",
        "TotalCount": 4
    }
}
```

