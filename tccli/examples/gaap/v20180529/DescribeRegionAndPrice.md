**Example 1: 获取源站区域和带宽梯度价格**

获取源站区域和带宽梯度价格

Input: 

```
tccli gaap DescribeRegionAndPrice --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DestRegionSet": [
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            }
        ],
        "RequestId": "xx",
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    2000,
                    0
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            }
        ],
        "Currency": "xx"
    }
}
```

**Example 2: 获取源站区域和带宽梯度价格2**



Input: 

```
tccli gaap DescribeRegionAndPrice --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DestRegionSet": [
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            }
        ],
        "RequestId": "xx",
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    2000,
                    0
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            }
        ],
        "Currency": "xx"
    }
}
```

