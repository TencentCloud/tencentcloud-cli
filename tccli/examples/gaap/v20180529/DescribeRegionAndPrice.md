**Example 1: 示例**



Input: 

```
tccli gaap DescribeRegionAndPrice --cli-unfold-argument  \
    --IPAddressVersion IPv4 \
    --PackageType Thunder
```

Output: 
```
{
    "Response": {
        "BandwidthUnitPrice": [],
        "Currency": "",
        "DestRegionSet": [
            {
                "FeatureBitmap": 151,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "Hongkong",
                "RegionName": "中国香港",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "SoutheastAsia",
                "RegionName": "新加坡",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "Korea",
                "RegionName": "韩国首尔",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Europe",
                "RegionAreaName": "欧洲",
                "RegionId": "Europe",
                "RegionName": "德国法兰克福",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "NorthAmerica",
                "RegionAreaName": "北美洲",
                "RegionId": "NorthAmerica",
                "RegionName": "美国西部硅谷",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "WestIndia",
                "RegionName": "印度西部孟买",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "Thailand",
                "RegionName": "泰国曼谷",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "NorthAmerica",
                "RegionAreaName": "北美洲",
                "RegionId": "Virginia",
                "RegionName": "美国东部弗吉尼亚",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "Japan",
                "RegionName": "日本东京",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "Taipei",
                "RegionName": "中国台北",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "SL_AZURE_NorthUAE",
                "RegionName": "阿联酋迪拜(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Oceania",
                "RegionAreaName": "大洋洲",
                "RegionId": "SL_AZURE_EastAUS",
                "RegionName": "澳大利亚东部悉尼(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "NorthAmerica",
                "RegionAreaName": "北美洲",
                "RegionId": "SL_AZURE_NorthCentralUSA",
                "RegionName": "美国中北部伊利诺斯(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "SL_AZURE_SouthIndia",
                "RegionName": "印度南部金奈(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "SouthAmerica",
                "RegionAreaName": "南美洲",
                "RegionId": "SL_AZURE_SouthBrazil",
                "RegionName": "巴西南部圣保罗(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Africa",
                "RegionAreaName": "非洲",
                "RegionId": "SL_AZURE_NorthZAF",
                "RegionName": "南非北部约翰内斯堡(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "SL_AZURE_SoutheastAsia",
                "RegionName": "新加坡（合作节点）",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Europe",
                "RegionAreaName": "欧洲",
                "RegionId": "SL_AZURE_CentralFrance",
                "RegionName": "法国中部巴黎(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Europe",
                "RegionAreaName": "欧洲",
                "RegionId": "SL_AZURE_SouthEngland",
                "RegionName": "英国南部伦敦(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "NorthAmerica",
                "RegionAreaName": "北美洲",
                "RegionId": "SL_AZURE_EastUS",
                "RegionName": "美国东部弗吉尼亚(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "NorthAmerica",
                "RegionAreaName": "北美洲",
                "RegionId": "SL_AZURE_WestUS",
                "RegionName": "美国西部加利福尼亚(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "NorthAmerica",
                "RegionAreaName": "北美洲",
                "RegionId": "SL_AZURE_SouthCentralUSA",
                "RegionName": "美国南部德克萨斯(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "Jakarta",
                "RegionName": "印尼雅加达",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 79,
                "IDCType": "dc",
                "RegionArea": "NorthChina",
                "RegionAreaName": "中国大陆-华北",
                "RegionId": "Beijing",
                "RegionName": "北京（原中国大陆-华北大区）",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 79,
                "IDCType": "dc",
                "RegionArea": "EastChina",
                "RegionAreaName": "中国大陆-华东",
                "RegionId": "Shanghai",
                "RegionName": "上海（原中国大陆-华东大区）",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 79,
                "IDCType": "dc",
                "RegionArea": "SouthChina",
                "RegionAreaName": "中国大陆-华南",
                "RegionId": "Guangzhou",
                "RegionName": "广州（原中国大陆-华南大区）",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 79,
                "IDCType": "dc",
                "RegionArea": "SouthwestChina",
                "RegionAreaName": "中国大陆-西南",
                "RegionId": "Chengdu",
                "RegionName": "成都（原中国大陆-西南地区）",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 7,
                "IDCType": "dc",
                "RegionArea": "Europe",
                "RegionAreaName": "欧洲",
                "RegionId": "SL_AZURE_NorwayEast",
                "RegionName": "挪威东部奥斯陆(合作节点)",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 71,
                "IDCType": "dc",
                "RegionArea": "SouthwestChina",
                "RegionAreaName": "中国大陆-西南",
                "RegionId": "Chongqing",
                "RegionName": "重庆",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 71,
                "IDCType": "dc",
                "RegionArea": "EastChina",
                "RegionAreaName": "中国大陆-华东",
                "RegionId": "Nanjing",
                "RegionName": "南京",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 135,
                "IDCType": "dc",
                "RegionArea": "SouthAmerica",
                "RegionAreaName": "南美洲",
                "RegionId": "SaoPaulo",
                "RegionName": "巴西",
                "SupportFeature": null
            },
            {
                "FeatureBitmap": 3,
                "IDCType": "dc",
                "RegionArea": "Asia",
                "RegionAreaName": "亚洲",
                "RegionId": "SL_AZURE_JapanEast",
                "RegionName": "日本东部埼玉县(合作节点)",
                "SupportFeature": null
            }
        ],
        "RequestId": "54f73e5b-0565-498c-bcc9-5605ca53b1be",
        "TotalCount": 32
    }
}
```

