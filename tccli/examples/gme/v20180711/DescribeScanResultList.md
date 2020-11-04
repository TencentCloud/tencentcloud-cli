**Example 1: 查询语音检测结果**



Input: 

```
tccli gme DescribeScanResultList --cli-unfold-argument  \
    --BizId 1400000000\
    --TaskIdList xxx\
    --Limit 20
```

Output: 
```
{
    "Data": [
        {
            "Code": 0,
            "DataId": "1400000000_test_data_id",
            "ScanFinishTime": 1566720906,
            "HitFlag": true,
            "Live": false,
            "Msg": "",
            "ScanPiece": [
                {
                    "DumpUrl": "",
                    "HitFlag": true,
                    "MainType": "abuse",
                    "Info": "",
                    "Offset": 0,
                    "Duration": 3400,
                    "PieceStartTime": 1574684231,
                    "ScanDetail": [
                        {
                            "EndTime": 1110,
                            "KeyWord": "xxx",
                            "Label": "abuse",
                            "Rate": "90.00",
                            "StartTime": 1110
                        },
                        {
                            "EndTime": 1380,
                            "KeyWord": "xxx",
                            "Label": "abuse",
                            "Rate": "90.00",
                            "StartTime": 930
                        },
                        {
                            "EndTime": 1560,
                            "KeyWord": "xxx",
                            "Label": "abuse",
                            "Rate": "90.00",
                            "StartTime": 930
                        },
                        {
                            "EndTime": 2820,
                            "KeyWord": "xxx",
                            "Label": "abuse",
                            "Rate": "90.00",
                            "StartTime": 2490
                        }
                    ]
                }
            ],
            "ScanStartTime": 1566720905,
            "Scenes": [
                "default"
            ],
            "Status": "Success",
            "TaskId": "xxx",
            "Url": "https://xxx/xxx.m4a"
        }
    ],
    "RequestId": "xxx"
}
```

