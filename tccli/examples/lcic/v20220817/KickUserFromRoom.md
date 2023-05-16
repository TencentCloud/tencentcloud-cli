**Example 1: 房间信息**

获取课堂房间信息

Input: 

```
tccli lcic KickUserFromRoom --cli-unfold-argument  \
    --RoomId 1 \
    --SdkAppId 1 \
    --UserId abc \
    --KickType 1 \
    --Duration 1
```

Output: 
```
{
    "Response": {
        "RequestId": "test"
    }
}
```

