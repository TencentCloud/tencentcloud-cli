**Example 1: 获取指定时刻的可用率地图信息 示例**



Input: 

```
tccli cat GetAvailRatioHistory --cli-unfold-argument  \
    --TaskId 260228 \
    --TimeStamp '2019-12-10 11:27:00'
```

Output: 
```
{
    "Response": {
        "AvgAvailRatio": 100,
        "AvgTime": 37,
        "LowestAvailRatio": 100,
        "LowestProvince": "北京(一区)",
        "LowestIsp": "腾讯云",
        "ProvinceData": [
            {
                "AvgAvailRatio": 100,
                "AvgTime": 37,
                "ProvinceName": "北京(一区)",
                "Mapkey": "beijing-1",
                "TimeStamp": "2019-12-10 11:27:00",
                "IspDetail": [
                    {
                        "IspName": "移动",
                        "AvailRatio": 100,
                        "AvgTime": 39
                    },
                    {
                        "IspName": "电信",
                        "AvailRatio": 100,
                        "AvgTime": 36
                    },
                    {
                        "IspName": "联通",
                        "AvailRatio": 100,
                        "AvgTime": 35
                    },
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 100,
                        "AvgTime": 38
                    }
                ],
                "Province": "beijing-1"
            }
        ],
        "AvgAvailRatio2": 100,
        "AvgTime2": 261,
        "LowestAvailRatio2": 100,
        "LowestProvince2": "莫斯科",
        "LowestIsp2": "腾讯云",
        "ProvinceData2": [
            {
                "AvgAvailRatio": 100,
                "AvgTime": 261,
                "ProvinceName": "莫斯科",
                "Mapkey": "moscow",
                "TimeStamp": "2019-12-10 11:27:00",
                "IspDetail": [
                    {
                        "IspName": "腾讯云",
                        "AvailRatio": 100,
                        "AvgTime": 261
                    }
                ],
                "Province": "moscow"
            }
        ],
        "RequestId": "d0791a07-6163-4e63-baad-97d244548d6f"
    }
}
```

