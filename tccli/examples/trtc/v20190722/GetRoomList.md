**Example 1: 获取房间列表**

获取TRTC房间列表

Input: 

```
tccli trtc GetRoomList --cli-unfold-argument  \
    --CallStatus 0 \
    --PageIndex 0 \
    --PageSize 10 \
    --UserId 123 \
    --StartTs 1570868198 \
    --EndTs 1570889798 \
    --SdkAppId 1400188366 \
    --RoomNum 666
```

Output: 
```
{
    "Response": {
        "Total": 33,
        "RoomList": [
            {
                "CommId": "1400188366_666_1570882159",
                "RoomNum": 666,
                "RoomStr": "666",
                "CreateTs": 1570882159,
                "DestroyTs": 1570883061,
                "Duration": 902,
                "CenterIp": "xx",
                "UserNum": 2,
                "Finished": true,
                "SourceType": 0
            },
            {
                "CommId": "1400188366_668_1570882148",
                "RoomNum": 668,
                "RoomStr": "668",
                "CreateTs": 1570882148,
                "DestroyTs": 1570883062,
                "Duration": 914,
                "CenterIp": "xx",
                "UserNum": 2,
                "Finished": true,
                "SourceType": 0
            },
            {
                "CommId": "1400188366_999_1570880470",
                "RoomNum": 999,
                "RoomStr": "999",
                "CenterIp": "xx",
                "CreateTs": 1570880470,
                "DestroyTs": 1570881122,
                "Duration": 652,
                "UserNum": 2,
                "Finished": true,
                "SourceType": 0
            }
        ],
        "RequestId": "0a4421a4-d118-489d-8c7a-6ab53bbb03bf"
    }
}
```

