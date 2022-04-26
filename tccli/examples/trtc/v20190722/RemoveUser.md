**Example 1: 移出用户**

将用户test1、test2从房间1234移出。

Input: 

```
tccli trtc RemoveUser --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 1234 \
    --UserIds test1 test2
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

