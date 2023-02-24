**Example 1: 创建签署流程**

通过文件发起单C流程，有文本控件、签署控件

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039******de6a \
    --FlowName 合同名称 \
    --NeedPreview False \
    --FlowDescription 测试签署流程的描述信息 \
    --Unordered False \
    --FlowType 劳动合同 \
    --Deadline 1604912664 \
    --ApproverVerifyType VerifyCheck \
    --CustomShowMap 合同名称:{合同名称} {发起方企业} {发起方姓名};国家:中国;发起方:{发起方企业};签署方1:  {签署方1企业};签署方2:  {签署方2企业}{签署方2姓名};签署方3:  {签署方3姓名} \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName xxx有限公司 \
    --Approvers.0.ApproverName 张三 \
    --Approvers.0.ApproverMobile 15912345678 \
    --Approvers.0.SignComponents.0.ComponentValue SealId \
    --Approvers.0.SignComponents.0.ComponentPosY 100 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.1.ComponentValue  \
    --Approvers.0.SignComponents.1.ComponentPosY 120 \
    --Approvers.0.SignComponents.1.ComponentWidth 120 \
    --Approvers.0.SignComponents.1.FileIndex 0 \
    --Approvers.0.SignComponents.1.ComponentType SIGN_DATE \
    --Approvers.0.SignComponents.1.ComponentPage 1 \
    --Approvers.0.SignComponents.1.ComponentPosX 120 \
    --Approvers.0.SignComponents.1.ComponentHeight 120 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 185111111111 \
    --Approvers.1.SignComponents.0.ComponentValue  \
    --Approvers.1.SignComponents.0.ComponentPosY 100 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 100 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.SignComponents.1.ComponentValue  \
    --Approvers.1.SignComponents.1.ComponentPosY 120 \
    --Approvers.1.SignComponents.1.ComponentWidth 120 \
    --Approvers.1.SignComponents.1.FileIndex 0 \
    --Approvers.1.SignComponents.1.ComponentType SIGN_DATE \
    --Approvers.1.SignComponents.1.ComponentPage 1 \
    --Approvers.1.SignComponents.1.ComponentPosX 120 \
    --Approvers.1.SignComponents.1.ComponentHeight 120 \
    --FileIds 61a82f0*******c2d0d807 \
    --Components.0.ComponentValue 自定义单行文本内容 \
    --Components.0.ComponentPosY 100 \
    --Components.0.ComponentWidth 100 \
    --Components.0.FileIndex 0 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 100 \
    --Components.0.ComponentHeight 100 \
    --Components.0.ComponentExtra {"FontSize":20} \
    --Components.1.ComponentValue 自定义多行文本内容 \
    --Components.1.ComponentPosY 100 \
    --Components.1.ComponentWidth 100 \
    --Components.1.FileIndex 0 \
    --Components.1.ComponentType MULTI_LINE_TEXT \
    --Components.1.ComponentPage 1 \
    --Components.1.ComponentPosX 100 \
    --Components.1.ComponentHeight 100 \
    --Components.1.ComponentExtra {"FontSize":20}
```

Output: 
```
{
    "Response": {
        "FlowId": "61a82f0c********0d807",
        "PreviewUrl": "",
        "RequestId": "requestId-xxx"
    }
}
```

**Example 2: 创建简单的签署流程**

通过文件发起单C流程，只有一个签署区域

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --UserData 字符串 \
    --FlowName 字符串 \
    --FlowDescription 字符串 \
    --NeedPreview false \
    --FlowType 字符串 \
    --Approvers.0.ApproverMobile 15912345678 \
    --Approvers.0.SignComponents.0.ComponentWidth 50 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentName 字符串 \
    --Approvers.0.SignComponents.0.OffsetX 11 \
    --Approvers.0.SignComponents.0.OffsetY 11 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 50 \
    --Approvers.0.SignComponents.0.ComponentPosY 50 \
    --Approvers.0.SignComponents.0.ComponentId 字符串 \
    --Approvers.0.SignComponents.0.ComponentHeight 50 \
    --Approvers.0.ApproverName 张三 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.NotifyType NONE \
    --Operator.UserId yDRtRUUgygqa2mtyUuO4zjEyckqC592v \
    --FileIds yDRI5UUgygsupv5oUuO4zjEESmE4Ip0s
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

