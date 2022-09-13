**Example 1: GetNatInstance 获取租户所有NAT实例**



Input: 

```
tccli cfw DescribeNatFwInstancesInfo --cli-unfold-argument  \
    --Filter.0.FilterType NatinsId \
    --Filter.0.FilterContent cfwnat-65d0d823,cfwnat-65d0d824 \
    --Filter.1.FilterType NatinsName \
    --Filter.1.FilterContent wytest \
    --Filter.2.FilterType FwMode \
    --Filter.2.FilterContent 1 \
    --Filter.3.FilterType Region \
    --Filter.3.FilterContent ap-guangzhou \
    --Filter.4.FilterType EipAddress \
    --Filter.4.FilterContent 1.13.19.217,1.13.16.20 \
    --Filter.5.FilterType VpcIp \
    --Filter.5.FilterContent 10.255.0.20,10.255.0.5 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NatinsLst": [
            {
                "BandWidth": 30,
                "EipAddress": [
                    "1.117.4.229",
                    "121.5.27.250"
                ],
                "FwMode": 0,
                "InFlowMax": 4985,
                "NatinsId": "cfwnat-f3250045",
                "NatinsName": "yw",
                "OutFlowMax": 14642,
                "Region": "ap-shanghai",
                "RegionZh": "上海",
                "Subnets": [
                    "subnet-cjxihpy1",
                    "subnet-1e34182d",
                    "subnet-5sx5vrcj",
                    "subnet-he9ba55f",
                    "subnet-0yd4fk0j",
                    "subnet-kdu0qj4t"
                ],
                "VpcIp": [
                    "10.255.6.36",
                    "10.255.6.37",
                    "10.255.6.21",
                    "10.255.6.18",
                    "10.255.6.19",
                    "10.255.5.28",
                    "10.255.5.18",
                    "10.255.5.19"
                ],
                "RegionDetail": "西南地区",
                "ZoneZh": "重庆一区",
                "ZoneZhBak": "重庆一区"
            }
        ],
        "Total": 1,
        "RequestId": "50e39f16-3b3a-4c66-b76e-1705449ba828"
    }
}
```

