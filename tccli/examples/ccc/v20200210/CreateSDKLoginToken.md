**Example 1: 创建 SDK 登录 Token**

创建 SDK 登录 Token

Input: 

```
tccli ccc CreateSDKLoginToken --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SeatUserId FooOrBar@tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "Token": "6bb56a09278740bc80c5dc6dab783eff",
        "SdkURL": "https://29294-22989-29805-29810.cdn-go.cn/tccc-agent-sdk/latest/",
        "ExpiredTime": 1601371974
    }
}
```

