**Example 1: 查询房间维度每天计费用量**

查询2022-11-24到2022-11-25的互动白板房间计费用量

Input: 

```
tccli tiw DescribeTIWRoomDailyUsage --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --SubProduct sp_tiw_board \
    --Limit 20 \
    --StartTime 2022-11-24 \
    --Offset 0 \
    --EndTime 2022-11-25
```

Output: 
```
{
    "Response": {
        "RequestId": "916f3549-8e91-467c-afcb-b8dacf188e12",
        "Usages": [
            {
                "Time": "2022-11-24",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "RoomID": 432946024,
                "Value": 5
            },
            {
                "Time": "2022-11-24",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "RoomID": 523696026,
                "Value": 60
            },
            {
                "Time": "2022-11-24",
                "SdkAppId": 1400000001,
                "SubProduct": "sp_tiw_board",
                "RoomID": 1284910005,
                "Value": 4
            }
        ],
        "Total": 3
    }
}
```

