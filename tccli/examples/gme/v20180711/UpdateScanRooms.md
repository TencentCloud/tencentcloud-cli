**Example 1: 更新用户自定义送检房间号**

更新用户自定义送检房间号

Input: 

```
tccli gme UpdateScanRooms --cli-unfold-argument  \
    --RoomIdRegex ^[0-9]*$ \
    --RoomIdString 0001,0002,0003 \
    --BizId 1400000000
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "af453fd2-c666-4401-ae96-03ec6a35fb61"
    }
}
```

