**Example 1: 获取全量接入点信息**

获取全量接入点信息，其中AVAILABLE是可以使用的接入点，UNAVAILABLE是不可以使用的接入点。

Input: 

```
tccli dc DescribeAccessPoints --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 6,
        "AccessPointSet": [
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-beijing",
                "AccessPointId": "ap-cn-beijing-hx",
                "State": "AVAILABLE",
                "Location": "北京市顺义区后沙峪镇中国航信高科技产业园 ",
                "AccessPointName": "北京航信"
            },
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-beijing",
                "AccessPointId": "ap-cn-beijing-jxq",
                "State": "AVAILABLE",
                "Location": "北京朝阳区电子城IT产业园 ",
                "AccessPointName": "北京万红路"
            },
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-beijing",
                "AccessPointId": "ap-cn-beijing-yz",
                "State": "UNAVAILABLE",
                "Location": "北京市大兴区亦庄开发区同济中路15号",
                "AccessPointName": "北京世纪互联1"
            },
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-beijing",
                "AccessPointId": "ap-cn-beijing-zj",
                "State": "AVAILABLE",
                "Location": "北京亦庄经济技术开发区博兴八路1号",
                "AccessPointName": "北京中金"
            },
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-beijing",
                "AccessPointId": "ap-cn-beijing-yf",
                "State": "UNAVAILABLE",
                "Location": "北京市海淀区丰慧中路11号安泰科技园C区B4栋",
                "AccessPointName": "北京永丰"
            },
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-beijing",
                "AccessPointId": "ap-cn-beijing-kc",
                "State": "AVAILABLE",
                "Location": "北京市经济技术开发区科创九街十五号",
                "AccessPointName": "北京科创"
            }
        ],
        "RequestId": "d591e41a-f3a5-4990-abf0-acdd88f238d9"
    }
}
```

**Example 2: 获取单地域接入点信息**

获取单地域接入点信息，其中AVAILABLE是可以使用的接入点，UNAVAILABLE是不可以使用的接入点。

Input: 

```
tccli dc DescribeAccessPoints --cli-unfold-argument  \
    --RegionId ap-chongqing
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "AccessPointSet": [
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-chongqing",
                "AccessPointId": "ap-cn-chongqing-yf",
                "State": "AVAILABLE",
                "Location": "重庆电信云福DC",
                "AccessPointName": "重庆云福"
            },
            {
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther",
                    "InternationalOperator"
                ],
                "RegionId": "ap-chongqing",
                "AccessPointId": "ap-cn-chongqing-yx",
                "State": "AVAILABLE",
                "Location": "重庆联通云祥DC",
                "AccessPointName": "重庆云祥"
            }
        ],
        "RequestId": "b6aa097b-3cd9-4c79-bf41-bb0d2427ffa1"
    }
}
```

