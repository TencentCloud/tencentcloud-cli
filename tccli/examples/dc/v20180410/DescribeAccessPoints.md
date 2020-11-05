**Example 1: Getting the information of all access points**

This example shows you how to get the information of all access points, where `AVAILABLE` indicates available access points and `UNAVAILABLE` indicates the unavailable ones.

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
                "Location": "TravelSky High-Tech Industrial Park, Houshayu Town, Shunyi District, Beijing",
                "AccessPointName": "TravelSky"
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
                "Location": "BEZ IT Park, Chaoyang District, Beijing",
                "AccessPointName": "Beijing Wanhong Road"
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
                "Location": "No. 15, Middle Tongji Road, Beijing Economic-Technological Development Area, Daxing District, Beijing",
                "AccessPointName": "Beijing 21Vianet 1"
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
                "Location": "No. 1, Bo'xing 8th Road, Beijing Economic-Technological Development Area, Beijing"
                "AccessPointName": "Beijing CICC"
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
                "Location": "Building B4, Zone C, AT&M Park, No. 11, Middle Fenghui Road, Haidian District, Beijing",
                "AccessPointName": "Beijing Yongfeng"
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
                "Location": "No. 15, Kechuang 9th Street, Beijing Economic-Technological Development Area, Beijing",
                "AccessPointName": "Beijing Kechuang"
            }
        ],
        "RequestId": "d591e41a-f3a5-4990-abf0-acdd88f238d9"
    }
}
```

**Example 2: Getting the information of access points in a specific region**

This example shows you how to get the information of access points in a specific region, where `AVAILABLE` indicates available access points and `UNAVAILABLE` indicates the unavailable ones.

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
                "Location": "Chongqing China Telecom Yunfu Data Center",
                "AccessPointName": "Chongqing Yunfu"
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
                "Location": "Chongqing China Unicom Yunxiang Data Center",
                "AccessPointName": "Chongqing Yunxiang"
            }
        ],
        "RequestId": "b6aa097b-3cd9-4c79-bf41-bb0d2427ffa1"
    }
}
```

