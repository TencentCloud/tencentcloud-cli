**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveAvatarRoom --cli-unfold-argument  \
    --Name live \
    --Operator admin
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "RoomId": "10002"
    }
}
```

**Example 2: 交互模式测试**



Input: 

```
tccli live CreateLiveAvatarRoom --cli-unfold-argument  \
    --Name 交互房间测试 \
    --AvatarKey 461d120836d649798cc5e1a3daa64c1d \
    --TimbreKey live_stream_female1 \
    --LiveMode INTERACT
```

Output: 
```
{
    "Response": {
        "RoomId": "2147485664",
        "RequestId": "0bf62c08-b542-466b-b500-5b55e4beecd1"
    }
}
```

