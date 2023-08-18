**Example 1: 创建只有个人C端签署, 签署人需要人脸校验认证的合同流程  (单C & 绝对定位  & 人脸校验  & 签名)**

1. 只有一个个人C端参与人 (Approvers只有一个ApproverInfo元素)
2. 签署区的指定通过绝对定位表达 (SignComponents中Component元素指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式)
3. C端参与人只有一个签名签署控件(SignComponents只有一个Component元素, 且这个元素的ComponentType是SIGN_SIGNATURE)
4. C端签署人需要人脸校验来签署合同 (ApproverSignTypes属性设置成[1]表示只能通过人脸识别校验来签署合同)

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 单个个人签署方合同示例 \
    --FlowType 保证书 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.ApproverSignTypes 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk
```

Output: 
```
{
    "Response": {
        "FlowId": "yDRsDUUgyg1aczxtUuNAW8Cx4WsAiEB5",
        "PreviewUrl": "",
        "RequestId": "43b9474a-c909-4d89-aa7b-3632f02fa8a4"
    }
}
```

**Example 2: 处方单场景(处方单 & 关键字定位)**

1. 处方单场景的"典子谦"医生需要自动签(典子谦参与人的ApproverType设置成7, 并且AutoSignScene设置成E_PRESCRIPTION_AUTO_SIGN表明是处方单场景)
2. 处方单的患者张三需要手工签署(张三参与人的ApproverType设置成1)
3. 双方签署方的签署控件都是通过关键字生成(典子谦签署区GenerateMode设置成KEYWORD并且ComponentId设置成关键字"处方医生", 张三签署区GenerateMode设置成KEYWORD并且ComponentId设置成关键字"患者签名" )
4. 不给合同签署方发送短信  (NotifyType设置成NONE)

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Approvers.0.ApproverIdCardNumber 620000198802020000 \
    --Approvers.0.ApproverIdCardType ID_CARD \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverType 7 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.ComponentId 处方医生 \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ComponentValue  \
    --Approvers.0.SignComponents.0.ComponentWidth 200 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentPosX 0 \
    --Approvers.0.SignComponents.0.ComponentPosY 0 \
    --Approvers.0.SignComponents.0.GenerateMode KEYWORD \
    --Approvers.0.SignComponents.0.OffsetX 80 \
    --Approvers.1.ApproverIdCardNumber 37000019890303000X \
    --Approvers.1.ApproverIdCardType ID_CARD \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.SignComponents.0.ComponentId 患者签名 \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentValue  \
    --Approvers.1.SignComponents.0.ComponentWidth 200 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.GenerateMode KEYWORD \
    --Approvers.1.SignComponents.0.OffsetX 80 \
    --Approvers.1.SignComponents.0.ComponentPosX 0 \
    --Approvers.1.SignComponents.0.ComponentPosY 0 \
    --Unordered True \
    --AutoSignScene E_PRESCRIPTION_AUTO_SIGN \
    --FileIds yDwqpUUckp3yptnhUxknKKxRmjIJ7ZHf \
    --FlowName 处方87235号 \
    --Operator.UserId 19561039c99fe825a934a132520fde6a
```

Output: 
```
{
    "Response": {
        "FlowId": "yDRsDUUgyg1aczxtUuNAW8Cx4WsAiEB5",
        "PreviewUrl": "",
        "RequestId": "43b9474a-c909-4d89-aa7b-3632f02fa8a4"
    }
}
```

