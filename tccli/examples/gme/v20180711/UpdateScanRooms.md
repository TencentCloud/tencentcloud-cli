**Example 1: 更新用户自定义送检房间号**



Input: 

```
tccli gme UpdateScanRooms --cli-unfold-argument  \
    --RoomIdRegex xx \
    --RoomIdString xx \
    --BizId 1
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "xx"
    }
}
```

