**Example 1: 查询语音检测结果**

查询语音检测结果

Input: 

```
tccli gme DescribeScanResultList --cli-unfold-argument  \
    --BizId 1400000000 \
    --TaskIdList 6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b \
    --Limit 20
```

Output: 
```
{
    "Response": {
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
                        "RoomId": "123",
                        "OpenId": "123",
                        "Info": "",
                        "Offset": 0,
                        "Duration": 3400,
                        "PieceStartTime": 1574684231,
                        "ScanDetail": [
                            {
                                "EndTime": 1110,
                                "KeyWord": "违规字",
                                "Label": "abuse",
                                "Rate": "90.00",
                                "StartTime": 1110
                            },
                            {
                                "EndTime": 1380,
                                "KeyWord": "违规字",
                                "Label": "abuse",
                                "Rate": "90.00",
                                "StartTime": 930
                            },
                            {
                                "EndTime": 1560,
                                "KeyWord": "违规字",
                                "Label": "abuse",
                                "Rate": "90.00",
                                "StartTime": 930
                            },
                            {
                                "EndTime": 2820,
                                "KeyWord": "违规字",
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
                "BizId": 123456789,
                "TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b",
                "Url": "https://xxx/xxx.m4a"
            }
        ],
        "RequestId": "863a8976-4d76-4481-9789-c631226f2475"
    }
}
```

