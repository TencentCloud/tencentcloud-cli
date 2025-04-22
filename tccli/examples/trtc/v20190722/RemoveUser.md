**Example 1: 移出用户**

将用户user_1、user_2从房间1001移出。

Input: 

```
tccli trtc RemoveUser --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 1001 \
    --UserIds user_1 user_2
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

