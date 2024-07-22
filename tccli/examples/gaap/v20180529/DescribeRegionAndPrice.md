**Example 1: 示例**



Input: 

```
tccli gaap DescribeRegionAndPrice --cli-unfold-argument  \
    --IPAddressVersion abc \
    --PackageType abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DestRegionSet": [
            {
                "RegionId": "abc",
                "RegionName": "abc",
                "RegionArea": "abc",
                "RegionAreaName": "abc",
                "IDCType": "abc",
                "FeatureBitmap": 1,
                "SupportFeature": {
                    "NetworkType": [
                        "abc"
                    ]
                }
            }
        ],
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0
                ],
                "BandwidthUnitPrice": 0,
                "DiscountBandwidthUnitPrice": 0
            }
        ],
        "Currency": "abc",
        "RequestId": "abc"
    }
}
```

