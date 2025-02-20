**Example 1: 查询指定EIP可调整带宽范围的上下限**



Input: 

```
tccli vpc DescribeAddressBandwidthRange --cli-unfold-argument  \
    --AddressIds eip-j12z7dfx eip-8b56zjpn
```

Output: 
```
{
    "Response": {
        "BandwidthRangeSet": [
            {
                "BandwidthLowerLimit": 1,
                "BandwidthUpperLimit": 2000,
                "ResourceId": "eip-8b56zjpn"
            },
            {
                "BandwidthLowerLimit": 1,
                "BandwidthUpperLimit": 100,
                "ResourceId": "eip-j12z7dfx"
            }
        ],
        "RequestId": "fc7f673e-8fca-43d0-a4f3-18e567cf6826"
    }
}
```

