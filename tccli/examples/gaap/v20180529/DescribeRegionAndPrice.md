**Example 1: Getting origin server region and tiered bandwidth prices**

This example shows you how to get the origin server region and tiered bandwidth prices.

Input: 

```
tccli gaap DescribeRegionAndPrice --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessRegionSet": [
            {
                "RegionId": "eu-moscow",
                "RegionName": "Russia"
            }
        ],
        "Currency": "CNY",
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 130
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 90
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 70
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 60
            },
            {
                "BandwidthRange": [
                    2000,
                    -1
                ],
                "BandwidthUnitPrice": 50
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

