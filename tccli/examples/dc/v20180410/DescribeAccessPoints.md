**Example 1: 获取全量接入点信息**

获取全量接入点信息。

Input: 

```
tccli dc DescribeAccessPoints --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessPointSet": [
            {
                "AccessPointName": "新加坡-C-泰戈尔",
                "AccessPointId": "ap-singapore-c-tagore",
                "City": "新加坡",
                "Area": "其它",
                "RegionId": "ap-singapore",
                "Location": "新加坡Dodid泰戈尔AC",
                "Address": "71 Tagore Ln,Singapore 787496",
                "Coordinate": {
                    "Lat": 1.3885116,
                    "Lng": 103.8277551
                },
                "AccessPointType": "VXLAN",
                "LineOperator": [
                    "InternationalOperator"
                ],
                "AvailablePortType": [
                    "1000BASE-LX",
                    "1000BASE-ZX",
                    "10GBASE-LR",
                    "10GBASE-ZR",
                    "100GBASE-LR4L",
                    "100GBASE-LR4",
                    "100GBASE-40KM",
                    "QSFPDD-400G-FR4",
                    "QSFPDD-400G-LR4"
                ],
                "AvailablePortInfo": [
                    {
                        "InternationalName": "1000BASE-LX",
                        "Specification": 1000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "1000BASE-ZX",
                        "Specification": 1000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "10GBASE-LR",
                        "Specification": 10000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "10GBASE-ZR",
                        "Specification": 10000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "100GBASE-LR4L",
                        "Specification": 100000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "100GBASE-LR4",
                        "Specification": 100000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "100GBASE-40KM",
                        "Specification": 100000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "QSFPDD-400G-FR4",
                        "Specification": 400000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "QSFPDD-400G-LR4",
                        "Specification": 400000,
                        "PortType": "X"
                    }
                ],
                "State": "AVAILABLE"
            }
        ],
        "RequestId": "b6aa097b-3cd9-4c79-bf41-bb0d2427ffa2",
        "TotalCount": 98
    }
}
```

**Example 2: 获取指定地域接入点信息**

获取指定地域接入点信息。

Input: 

```
tccli dc DescribeAccessPoints --cli-unfold-argument  \
    --RegionId ap-chongqing
```

Output: 
```
{
    "Response": {
        "AccessPointSet": [
            {
                "AccessPointName": "重庆-A-泰和",
                "AccessPointId": "ap-chongqing-a-th",
                "City": "重庆",
                "Area": "西南",
                "RegionId": "ap-chongqing",
                "Location": "重庆腾讯泰和DC",
                "Address": "重庆市北碚区水土镇高新技术产业园泰和路777号",
                "Coordinate": {
                    "Lat": 29.790833,
                    "Lng": 106.523072
                },
                "AccessPointType": "VXLAN",
                "LineOperator": [
                    "ChinaTelecom",
                    "ChinaMobile",
                    "ChinaUnicom",
                    "In-houseWiring",
                    "ChinaOther"
                ],
                "AvailablePortType": [
                    "1000BASE-LX",
                    "1000BASE-T",
                    "1000BASE-ZX",
                    "10GBASE-LR",
                    "10GBASE-ZR",
                    "100GBASE-LR4L",
                    "100GBASE-LR4",
                    "100GBASE-40KM",
                    "QSFPDD-400G-FR4",
                    "QSFPDD-400G-LR4"
                ],
                "AvailablePortInfo": [
                    {
                        "InternationalName": "1000BASE-LX",
                        "Specification": 1000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "1000BASE-T",
                        "Specification": 1000,
                        "PortType": "T"
                    },
                    {
                        "InternationalName": "1000BASE-ZX",
                        "Specification": 1000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "10GBASE-LR",
                        "Specification": 10000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "10GBASE-ZR",
                        "Specification": 10000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "100GBASE-LR4L",
                        "Specification": 100000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "100GBASE-LR4",
                        "Specification": 100000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "100GBASE-40KM",
                        "Specification": 100000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "QSFPDD-400G-FR4",
                        "Specification": 400000,
                        "PortType": "X"
                    },
                    {
                        "InternationalName": "QSFPDD-400G-LR4",
                        "Specification": 400000,
                        "PortType": "X"
                    }
                ],
                "State": "AVAILABLE"
            }
        ],
        "RequestId": "b6aa097b-3cd9-4c79-bf41-bb0d2427ffa3",
        "TotalCount": 3
    }
}
```

