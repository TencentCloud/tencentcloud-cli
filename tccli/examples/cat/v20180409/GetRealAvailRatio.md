**Example 1: 获取实时可用率信息 示例**



Input: 

```
tccli cat GetRealAvailRatio --cli-unfold-argument  \
    --TaskId 253632
```

Output: 
```
{
    "Response": {
        "AvgAvailRatio": 100,
        "AvgTime": 123.32,
        "LowestAvailRatio": 100,
        "LowestProvince": "天津",
        "LowestIsp": "联通",
        "ProvinceData": [
            {
                "AvgAvailRatio": 100,
                "AvgTime": 202.5,
                "ProvinceName": "安徽",
                "Mapkey": "anHui",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 100,
                        "AvgTime": 202.5
                    }
                ],
                "Province": "anhui"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 201,
                "ProvinceName": "辽宁",
                "Mapkey": "liaoNing",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 100,
                        "AvgTime": 201
                    }
                ],
                "Province": "liaoning"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 83.5,
                "ProvinceName": "上海",
                "Mapkey": "shangHai",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 100,
                        "AvgTime": 118
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 65.5
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 100,
                        "AvgTime": 67
                    }
                ],
                "Province": "sh"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 143.17,
                "ProvinceName": "四川",
                "Mapkey": "siChuan",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 100,
                        "AvgTime": 82
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 226
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 100,
                        "AvgTime": 121.5
                    }
                ],
                "Province": "sichuan"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 45.5,
                "ProvinceName": "天津",
                "Mapkey": "tianJin",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 100,
                        "AvgTime": 66.5
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 14.5
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 100,
                        "AvgTime": 55.5
                    }
                ],
                "Province": "tj"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 89.5,
                "ProvinceName": "重庆",
                "Mapkey": "chongQing",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 89.5
                    }
                ],
                "Province": "chongqing"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 238,
                "ProvinceName": "福建",
                "Mapkey": "fuJian",
                "TimeStamp": "2019-12-12 18:31:00",
                "IspDetail": [
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 238
                    }
                ],
                "Province": "fujian"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 91.25,
                "ProvinceName": "广东",
                "Mapkey": "guangDong",
                "TimeStamp": "2019-12-12 18:31:00",
                "IspDetail": [
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 91
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 100,
                        "AvgTime": 91.5
                    }
                ],
                "Province": "gd"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 219,
                "ProvinceName": "贵州",
                "Mapkey": "guiZhou",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 219
                    }
                ],
                "Province": "guizhou"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 209.67,
                "ProvinceName": "湖南",
                "Mapkey": "huNan",
                "TimeStamp": "2019-12-12 18:31:00",
                "IspDetail": [
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 209.67
                    }
                ],
                "Province": "hunan"
            },
            {
                "AvgAvailRatio": 100,
                "AvgTime": 61,
                "ProvinceName": "浙江",
                "Mapkey": "zheJiang",
                "TimeStamp": "2019-12-12 18:32:00",
                "IspDetail": [
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 61
                    }
                ],
                "Province": "zj"
            }
        ],
        "AvgAvailRatio2": 100,
        "AvgTime2": 0,
        "LowestAvailRatio2": 100,
        "LowestProvince2": "",
        "LowestIsp2": "",
        "ProvinceData2": [],
        "RequestId": "e15b251e-60c5-48af-8213-159315cd0361"
    }
}
```

