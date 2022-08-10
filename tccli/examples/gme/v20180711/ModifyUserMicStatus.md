**Example 1: 修改用户麦克风属性**



Input: 

```
tccli gme ModifyUserMicStatus --cli-unfold-argument  \
    --RoomId xx \
    --BizId 0 \
    --Users.0.Uid 0 \
    --Users.0.EnableMic 0
```

Output: 
```
{
    "Response": {
        "Result": 0,
        "ErrMsg": "xx",
        "RequestId": "xx"
    }
}
```

