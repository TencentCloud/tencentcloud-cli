**Example 1: 告警列表**

成功响应

Input: 

```
tccli weilingwith DescribeAlarmList --cli-unfold-argument  \
    --BeginTime 1693416387 \
    --EndTime 1693416987 \
    --PageNumber 1 \
    --PageSize 1 \
    --WorkspaceId 1016 \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2
```

Output: 
```
{
    "Response": {
        "RequestId": "bb4a6274-71b1-4107-98a2-06819376fb4e",
        "Result": {
            "AlarmInfoSet": [
                {
                    "AppId": 0,
                    "Desc": "水量使用超限",
                    "DeviceName": "20楼水表",
                    "Echo": "",
                    "Extend": "x-json:{\"alarmLevel\":3,\"alarmValue\":13730945.6}",
                    "ExtendOne": "x-json:",
                    "ExtendTwo": "x-json:",
                    "HandlePersonSet": [],
                    "HandleRecordSet": [],
                    "Id": "0c6ec1cc-25d6-43bc-96b1-6b4131f1771a",
                    "Level": 3,
                    "LevelName": "严重",
                    "Position": "滨海大厦-7F",
                    "ReportImg": {
                        "Data": "",
                        "Type": 0
                    },
                    "Status": "unprocessed",
                    "SubType": "water_limit",
                    "SubTypeName": "水量使用超限",
                    "Time": 1693416976,
                    "Type": "energy",
                    "TypeName": "能源",
                    "WID": "b1fd7aa3-4407-4b82-9dc3-aff9b3034a9f",
                    "WorkspaceId": 1016
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalPage": 125,
            "TotalRow": 125
        }
    }
}
```

