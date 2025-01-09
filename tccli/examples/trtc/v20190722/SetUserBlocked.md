**Example 1: 设置音视频状态**

适用于主播/房主/管理员等通过后台禁言/解禁言某个用户的场景。

Input: 

```
tccli trtc SetUserBlocked --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RoomId 10006 \
    --UserId 29376 \
    --IsMute 1
```

Output: 
```
{
    "Response": {
        "RequestId": "44e494f6-8010-4bb2-9a9d-ba5fd191353a"
    }
}
```

