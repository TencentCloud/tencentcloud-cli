**Example 1: 获取源站区域和带宽梯度价格**

获取源站区域和带宽梯度价格

Input: 

```
tccli gaap DescribeRegionAndPrice --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 26,
        "Currency": "CNY",
        "RequestId": "61b759bb-3d4c-4d7d-a8dc-a7bf2be63328",
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 130,
                "DiscountBandwidthUnitPrice": 130
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 90,
                "DiscountBandwidthUnitPrice": 90
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 70,
                "DiscountBandwidthUnitPrice": 70
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 60,
                "DiscountBandwidthUnitPrice": 60
            },
            {
                "BandwidthRange": [
                    2000,
                    -1
                ],
                "BandwidthUnitPrice": 50,
                "DiscountBandwidthUnitPrice": 50
            }
        ],
        "DestRegionSet": [
            {
                "RegionId": "NorthChina",
                "RegionName": "中国大陆-华北大区",
                "RegionArea": "NorthChina",
                "RegionAreaName": "中国大陆-华北",
                "IDCType": "dc"
            }
        ]
    }
}
```

