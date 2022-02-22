**Example 1: 签署流程文档**



Input: 

```
tccli essbasic SignFlow --cli-unfold-argument  \
    --ApproveMessage 同意 \
    --VerifyChannel FACEID \
    --Caller.SubOrganizationId 子机构账号 \
    --Caller.ApplicationId 应用号 \
    --Caller.OperatorId  \
    --FlowId bfe97ea80ae05bb5912aa43b87c6cc5f \
    --SignSeals.0.SealContent bass64格式图片内容 \
    --SignSeals.0.SealId  \
    --SignSeals.0.SignType SIGN_SIGNATURE \
    --SignSeals.0.ComponentId ae25dfda347710493e8b27e68b286f17 \
    --SignSeals.0.FileIndex 0 \
    --VerifyResult 核身票据 \
    --SourceIp 8.8.8.8 \
    --SignId 
```

Output: 
```
{
    "Response": {
        "Status": "SUCCESS",
        "RequestId": "s1611211923633441897"
    }
}
```

