**Example 1: 获取一天的整体可用率信息 示例**



Input: 

```
tccli cat GetDailyAvailRatio --cli-unfold-argument  \
    --TaskId 260228
```

Output: 
```
{
    "Response": {
        "AvgAvailRatio": 0,
        "AvgTime": 1000.31,
        "LowestAvailRatio": 0,
        "LowestProvince": "",
        "ProvinceData": [
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.35,
                "ProvinceName": "北京(一区)",
                "Mapkey": "beijing-1",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.27
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.31
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.3
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.52
                    }
                ],
                "Province": "beijing-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.32,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.4
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.28
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.3
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.29
                    }
                ],
                "Province": "beijing-3"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.19,
                "ProvinceName": "重庆",
                "Mapkey": "chongQing",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.17
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.28
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.13
                    }
                ],
                "Province": "chongqing"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.18,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.24
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.16
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.15
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.17
                    }
                ],
                "Province": "guangzhou-3"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.15,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.15
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.17
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.14
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.15
                    }
                ],
                "Province": "guangzhou-4"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.79,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.8
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.78
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.77
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.8
                    }
                ],
                "Province": "shanghai-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.31,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.32
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.31
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.3
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.31
                    }
                ],
                "Province": "shanghai-3"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.32,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 0,
                        "AvgTime": 1000.32
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 0,
                        "AvgTime": 1000.34
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 0,
                        "AvgTime": 1000.31
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.31
                    }
                ],
                "Province": "shanghai-4"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.2,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.2
                    }
                ],
                "Province": "bangkok-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.08,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.08
                    }
                ],
                "Province": "germany-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.13,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.13
                    }
                ],
                "Province": "hongkong-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.3,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.3
                    }
                ],
                "Province": "hongkong-2"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.27,
                "ProvinceName": "江苏",
                "Mapkey": "jiangSu",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.27
                    }
                ],
                "Province": "jiangsu"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.16,
                "ProvinceName": "孟买",
                "Mapkey": "mumbai",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.16
                    }
                ],
                "Province": "mumbai"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.53,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.53
                    }
                ],
                "Province": "shanghai-2"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.3,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.3
                    }
                ],
                "Province": "silicon-v1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.32,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.32
                    }
                ],
                "Province": "silicon-v2"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.17,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.17
                    }
                ],
                "Province": "singapore-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.27,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.27
                    }
                ],
                "Province": "tianjin-1"
            },
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.25,
                "ProvinceName": "",
                "Mapkey": "",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.25
                    }
                ],
                "Province": "va"
            }
        ],
        "AvgAvailRatio2": 0,
        "AvgTime2": 1000.12,
        "LowestAvailRatio2": 0,
        "LowestProvince2": "莫斯科",
        "ProvinceData2": [
            {
                "AvgAvailRatio": 0,
                "AvgTime": 1000.12,
                "ProvinceName": "莫斯科",
                "Mapkey": "moscow",
                "TimeStamp": "2019-12-11 00:00:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 0,
                        "AvgTime": 1000.12
                    }
                ],
                "Province": "moscow"
            }
        ],
        "RequestId": "12f1f02c-fc67-4e47-9243-b906a541eeb9"
    }
}
```

