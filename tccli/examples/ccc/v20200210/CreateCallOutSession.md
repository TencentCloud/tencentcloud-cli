**Example 1: 外呼接口调用示例**

在不加载前端 SDK 的场景下，可以通过在后台触发此接口进行外呼，当前只支持通过手机端回拨外呼（先拨通客服手机），并且确认已经申请并通过添加外呼白名单。

Input: 

```
tccli ccc CreateCallOutSession --cli-unfold-argument  \
    --IsForceUseMobile true \
    --Callee 008612300000000 \
    --Uui fooandbar \
    --UserId FooOrBar@tencent.com \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "SessionId": "6bb56a09278740bc80c5dc6dab783eff"
    }
}
```

