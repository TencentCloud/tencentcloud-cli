**Example 1: 发送流程**



Input: 

```
tccli essbasic SendFlowUrl --cli-unfold-argument  \
    --Mobile 1521981**** \
    --IsLastApprover False \
    --UserId e3e303228df9327c3e1661e1ebff7**** \
    --VerifyChannel FACEID \
    --PreReadTime 20 \
    --JumpUrl https://www.qq.com \
    --Caller.OperatorId e3e303228df9327c3e1661e1ebff7e1b \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --SignComponents.0.ComponentPosY 100 \
    --SignComponents.0.ComponentType SIGN_SIGNATURE \
    --SignComponents.0.FileIndex 0 \
    --SignComponents.0.ComponentWidth 100 \
    --SignComponents.0.ComponentPosX 100 \
    --SignComponents.0.ComponentRequired True \
    --SignComponents.0.ComponentHeight 100 \
    --SignComponents.0.ComponentPage 1 \
    --SignComponents.1.ComponentPosY 200 \
    --SignComponents.1.ComponentType SIGN_SIGNATURE \
    --SignComponents.1.FileIndex 0 \
    --SignComponents.1.ComponentWidth 100 \
    --SignComponents.1.ComponentPosX 200 \
    --SignComponents.1.ComponentRequired True \
    --SignComponents.1.ComponentHeight 100 \
    --SignComponents.1.ComponentPage 1 \
    --SignComponents.2.ComponentPosY 300 \
    --SignComponents.2.ComponentType SIGN_DATE \
    --SignComponents.2.FileIndex 1 \
    --SignComponents.2.ComponentWidth 100 \
    --SignComponents.2.ComponentPosX 300 \
    --SignComponents.2.ComponentRequired True \
    --SignComponents.2.ComponentHeight 100 \
    --SignComponents.2.ComponentPage 1 \
    --SignComponents.3.ComponentPosY 200 \
    --SignComponents.3.ComponentType SIGN_SIGNATURE \
    --SignComponents.3.FileIndex 2 \
    --SignComponents.3.ComponentWidth 100 \
    --SignComponents.3.ComponentPosX 200 \
    --SignComponents.3.ComponentRequired True \
    --SignComponents.3.ComponentHeight 100 \
    --SignComponents.3.ComponentPage 2 \
    --SignComponents.4.ComponentPosY 200 \
    --SignComponents.4.ComponentType SIGN_SIGNATURE \
    --SignComponents.4.FileIndex 3 \
    --SignComponents.4.ComponentWidth 100 \
    --SignComponents.4.ComponentPosX 200 \
    --SignComponents.4.ComponentRequired True \
    --SignComponents.4.ComponentHeight 100 \
    --SignComponents.4.ComponentPage 3 \
    --SignComponents.5.ComponentPosY 200 \
    --SignComponents.5.ComponentType SIGN_SIGNATURE \
    --SignComponents.5.FileIndex 4 \
    --SignComponents.5.ComponentWidth 100 \
    --SignComponents.5.ComponentPosX 200 \
    --SignComponents.5.ComponentRequired True \
    --SignComponents.5.ComponentHeight 100 \
    --SignComponents.5.ComponentPage 4 \
    --SignComponents.6.ComponentPosY 200 \
    --SignComponents.6.ComponentType SIGN_SIGNATURE \
    --SignComponents.6.FileIndex 5 \
    --SignComponents.6.ComponentWidth 100 \
    --SignComponents.6.ComponentPosX 200 \
    --SignComponents.6.ComponentRequired True \
    --SignComponents.6.ComponentHeight 100 \
    --SignComponents.6.ComponentPage 5 \
    --SignComponents.7.ComponentPosY 200 \
    --SignComponents.7.ComponentType SIGN_SIGNATURE \
    --SignComponents.7.FileIndex 6 \
    --SignComponents.7.ComponentWidth 100 \
    --SignComponents.7.ComponentPosX 200 \
    --SignComponents.7.ComponentRequired True \
    --SignComponents.7.ComponentHeight 100 \
    --SignComponents.7.ComponentPage 6 \
    --SignComponents.8.ComponentPosY 200 \
    --SignComponents.8.ComponentType SIGN_SIGNATURE \
    --SignComponents.8.FileIndex 7 \
    --SignComponents.8.ComponentWidth 100 \
    --SignComponents.8.ComponentPosX 200 \
    --SignComponents.8.ComponentRequired True \
    --SignComponents.8.ComponentHeight 100 \
    --SignComponents.8.ComponentPage 7 \
    --FlowId b334e0cbdf76eb21b7c4cd75e0219**** \
    --Deadline 1609927200 \
    --SubOrganizationId 732aaefa78c439d726f541b89c49e**** \
    --IsFullText True \
    --CanOffLine True \
    --CallbackUrl https://www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609919003607383165",
        "SignUrl": "https://essurl.cn/CN6eomUBge",
        "SignId": "361d2e5b411f3c7c16d082169d49a747"
    }
}
```

