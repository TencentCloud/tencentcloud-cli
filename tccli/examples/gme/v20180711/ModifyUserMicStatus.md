**Example 1: 修改用户麦克风属性**

修改用户麦克风属性

Input: 

```
tccli gme ModifyUserMicStatus --cli-unfold-argument  \
    --BizId 1400000000 \
    --RoomId 300 \
    --Users.0.Uid 1111 \
    --Users.0.EnableMic 1 \
    --Users.0.StrUid 
```

Output: 
```
{
    "Response": {
        "Result": 0,
        "ErrMsg": "",
        "RequestId": "f2c37dfd-56c9-400e-9fbc-705db7a74af8"
    }
}
```

