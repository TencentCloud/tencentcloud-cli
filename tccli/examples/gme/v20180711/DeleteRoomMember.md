**Example 1: 剔除房间内某两个用户**

剔除房间内某两个用户

Input: 

```
tccli gme DeleteRoomMember --cli-unfold-argument  \
    --DeleteType 2 \
    --RoomId 100 \
    --BizId 1400000000 \
    --Uids 2 1
```

Output: 
```
{
    "Response": {
        "RequestId": "dfe39c29-ce97-44df-ba79-7d947d465694",
        "DeleteResult": {
            "Code": 0,
            "ErrorMsg": ""
        }
    }
}
```

