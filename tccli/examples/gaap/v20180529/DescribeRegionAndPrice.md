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
                "RegionName": "中国大陆-华北大区"
            },
            {
                "RegionId": "EastChina",
                "RegionName": "中国大陆-华东大区"
            },
            {
                "RegionId": "SouthChina",
                "RegionName": "中国大陆-华南大区"
            },
            {
                "RegionId": "SouthwestChina",
                "RegionName": "中国大陆-西南大区"
            },
            {
                "RegionId": "Hongkong",
                "RegionName": "中国香港"
            },
            {
                "RegionId": "SoutheastAsia",
                "RegionName": "新加坡"
            },
            {
                "RegionId": "Korea",
                "RegionName": "韩国首尔"
            },
            {
                "RegionId": "Europe",
                "RegionName": "德国法兰克福"
            },
            {
                "RegionId": "NorthAmerica",
                "RegionName": "美国西部硅谷"
            },
            {
                "RegionId": "Canada",
                "RegionName": "加拿大"
            },
            {
                "RegionId": "WestIndia",
                "RegionName": "印度西部孟买"
            },
            {
                "RegionId": "Thailand",
                "RegionName": "泰国曼谷"
            },
            {
                "RegionId": "Virginia",
                "RegionName": "美国东部弗吉尼亚"
            },
            {
                "RegionId": "Russia",
                "RegionName": "俄罗斯"
            },
            {
                "RegionId": "Japan",
                "RegionName": "日本东京"
            },
            {
                "RegionId": "Taipei",
                "RegionName": "中国台北"
            },
            {
                "RegionId": "SL_AZURE_NorthUAE",
                "RegionName": "阿联酋迪拜(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_EastAUS",
                "RegionName": "澳大利亚东部悉尼(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_NorthCentralUSA",
                "RegionName": "美国伊利诺斯州(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_SouthIndia",
                "RegionName": "印度南部金奈(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_SouthBrazil",
                "RegionName": "巴西南部圣保罗(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_SoutheastAsia",
                "RegionName": "新加坡(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_CentralFrance",
                "RegionName": "法国中部巴黎(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_SouthEngland",
                "RegionName": "英国南部伦敦(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_EastUS",
                "RegionName": "美国东部弗吉尼亚(合作节点)"
            },
            {
                "RegionId": "SL_AZURE_WestUS",
                "RegionName": "美国西部加利福尼亚(合作节点)"
            }
        ]
    }
}
```

