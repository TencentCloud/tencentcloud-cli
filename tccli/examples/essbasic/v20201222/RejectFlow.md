**Example 1: 拒签流程文档**



Input: 

```
tccli essbasic RejectFlow --cli-unfold-argument  \
    --Caller.ApplicationId 应用号 \
    --Caller.SubOrganizationId 子机构账号 \
    --Caller.OperatorId  \
    --FlowId bfe97ea80ae05bb5912aa43b87c6cc5f \
    --RejectMessage 合同内容有误 \
    --VerifyResult 人脸核身票据 \
    --VerifyChannel FACEID \
    --SourceIp 8.8.8.8 \
    --SignId 
```

Output: 
```
{
    "Response": {
        "RequestId": "s1611216688526730856"
    }
}
```

