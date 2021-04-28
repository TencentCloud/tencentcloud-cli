**Example 1: 枚举地域**



Input: 

```
tccli ckafka DescribeRegion --cli-unfold-argument  \
    --Business 10
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "RegionId": 8,
                "RegionName": "北京",
                "AreaName": "华北地区",
                "RegionCode": "bj",
                "RegionCodeV3": "ap-beijing"
            },
            {
                "RegionId": 16,
                "RegionName": "成都",
                "AreaName": "西南地区",
                "RegionCode": "cd",
                "RegionCodeV3": "ap-chengdu"
            },
            {
                "RegionId": 19,
                "RegionName": "重庆",
                "AreaName": "西南地区",
                "RegionCode": "cq",
                "RegionCodeV3": "ap-chongqing"
            },
            {
                "RegionId": 5,
                "RegionName": "香港",
                "AreaName": "东南亚地区",
                "RegionCode": "hk",
                "RegionCodeV3": "ap-hongkong"
            },
            {
                "RegionId": 9,
                "RegionName": "新加坡",
                "AreaName": "东南亚地区",
                "RegionCode": "sg",
                "RegionCodeV3": "ap-singapore"
            },
            {
                "RegionId": 21,
                "RegionName": "孟买",
                "AreaName": "亚太地区",
                "RegionCode": "in",
                "RegionCodeV3": "ap-mumbai"
            },
            {
                "RegionId": 25,
                "RegionName": "东京",
                "AreaName": "亚太地区",
                "RegionCode": "jp",
                "RegionCodeV3": "ap-tokyo"
            },
            {
                "RegionId": 6,
                "RegionName": "多伦多",
                "AreaName": "北美地区",
                "RegionCode": "ca",
                "RegionCodeV3": "na-toronto"
            },
            {
                "RegionId": 15,
                "RegionName": "硅谷",
                "AreaName": "美国西部",
                "RegionCode": "usw",
                "RegionCodeV3": "na-siliconvalley"
            },
            {
                "RegionId": 22,
                "RegionName": "弗吉尼亚",
                "AreaName": "美国东部",
                "RegionCode": "use",
                "RegionCodeV3": "na-ashburn"
            }
        ],
        "RequestId": "fe2ba3b1-90bb-425d-abd4-08a62d0c3686"
    }
}
```

