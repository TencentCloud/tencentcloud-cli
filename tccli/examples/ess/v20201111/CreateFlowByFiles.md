**Example 1: 错误示例：签署人姓名格式传递错误，导致合同创建失败，不扣费用。**

1. 如果签署人姓名传递了非法的字符串，将会提示错误。
2. 合同发起失败，不会生成flowId。
3. 对于发起失败的合同，不会进行扣费。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 错误示例合同 \
    --FlowType 保证书 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.ApproverName 典子谦& \
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
        "Error": {
            "Code": "InvalidParameter.Name",
            "Message": "参数错误,姓名不符合规范,请修改后重试"
        },
        "RequestId": "s1692325082060040872"
    }
}
```

**Example 2: 创建一份本方企业和个人进行签署合同**

1. 签署方包括本方企业和个人（Approvers中有两个ApproverInfo元素）。
2. 本方企业签署前需要审核（将NeedSignReview设置为true）。
3. 本方企业的签署区仅具有一个印章签署控件：印章（SignComponents中有一个Component元素，印章（SIGN_SEAL）使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
4. C端参与者仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
5. 本流程包含两个抄送人，抄送人可查看合同信息（CcInfos中有两个CcInfo的信息）。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Unordered True \
    --FlowName B2C 待审核的&带有抄送人 \
    --FlowType 示例合同 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.PreReadTime 10 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 160 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --CcInfos.0.Name 李四 \
    --CcInfos.0.Mobile 15100000000 \
    --CcInfos.1.Name 王五 \
    --CcInfos.1.Mobile 13700000000 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk \
    --NeedSignReview True
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwqoUUckp3bkmc7UuPTimaxVoB5m1iD",
        "PreviewUrl": "",
        "RequestId": "s1692184714668577966"
    }
}
```

**Example 3: 创建一份涉及本方企业、他方企业和个人签署的三方无序签署合同**

1. 签署方包括本方企业、他方企业和个人（Approvers中有三个ApproverInfo元素）。
2. 本方企业的签署区仅具有一个印章签署控件：印章（SignComponents中有一个Component元素，印章（SIGN_SEAL）使用关键字定位方式，即GenerateMode = KEYWORD）。
3. 他方企业参与者仅具有一个印章签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SEAL，使用关键字定位方式，即GenerateMode = KEYWORD）。
4. C端参与者仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，使用关键字定位方式，即GenerateMode = KEYWORD）。
5. 本合同为无序签署（Unordered传递为true）。
6. 有关关键字定位PDF的创建方式，请参阅电子签开发者中心 -> 常见问题 -> PDF相关介绍。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName B2B2C关键字无序签署示例合同 \
    --FlowType 示例合同 \
    --Unordered True \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.PreReadTime 10 \
    --Approvers.0.SignComponents.0.GenerateMode KEYWORD \
    --Approvers.0.SignComponents.0.ComponentId Test \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPosX 0 \
    --Approvers.0.SignComponents.0.ComponentPosY 0 \
    --Approvers.0.SignComponents.0.ComponentPage 0 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.OffsetX 100.5 \
    --Approvers.0.SignComponents.0.OffsetY 200.5 \
    --Approvers.0.SignComponents.0.KeywordOrder Positive \
    --Approvers.0.SignComponents.0.KeywordPage 1 \
    --Approvers.0.SignComponents.0.RelativeLocation Middle \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 张三示例企业 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.PreReadTime 10 \
    --Approvers.1.SignComponents.0.GenerateMode KEYWORD \
    --Approvers.1.SignComponents.0.ComponentId Test1 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.1.SignComponents.0.ComponentPosX 0 \
    --Approvers.1.SignComponents.0.ComponentPosY 0 \
    --Approvers.1.SignComponents.0.ComponentPage 0 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.SignComponents.0.OffsetX 100.5 \
    --Approvers.1.SignComponents.0.OffsetY 200.5 \
    --Approvers.1.SignComponents.0.KeywordOrder Positive \
    --Approvers.1.SignComponents.0.KeywordPage 1 \
    --Approvers.1.SignComponents.0.RelativeLocation Middle \
    --Approvers.2.ApproverType 1 \
    --Approvers.2.NotifyType NONE \
    --Approvers.2.ApproverName 李四 \
    --Approvers.2.ApproverMobile 15100000000 \
    --Approvers.2.PreReadTime 10 \
    --Approvers.2.SignComponents.0.GenerateMode KEYWORD \
    --Approvers.2.SignComponents.0.ComponentId Test2 \
    --Approvers.2.SignComponents.0.FileIndex 0 \
    --Approvers.2.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.2.SignComponents.0.ComponentPosX 0 \
    --Approvers.2.SignComponents.0.ComponentPosY 0 \
    --Approvers.2.SignComponents.0.ComponentPage 0 \
    --Approvers.2.SignComponents.0.ComponentWidth 100 \
    --Approvers.2.SignComponents.0.ComponentHeight 100 \
    --Approvers.2.SignComponents.0.OffsetX 100.5 \
    --Approvers.2.SignComponents.0.OffsetY 200.5 \
    --Approvers.2.SignComponents.0.KeywordOrder Positive \
    --Approvers.2.SignComponents.0.KeywordPage 1 \
    --Approvers.2.SignComponents.0.RelativeLocation Middle \
    --FileIds yDwqYUUckp39gkfxUu14JJPxaTyM1ltq
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwqoUUckp3bkmmbUuPTimaq7zNEvxoX",
        "PreviewUrl": "",
        "RequestId": "s1692265794625568498"
    }
}
```

**Example 4: 创建一份涉及本方企业、他方企业和个人签署的三方有序签署合同**

1. 签署方包括本方企业、他方企业和个人（Approvers中有三个ApproverInfo元素）。
2. 本方企业的签署区包含两个签署控件：骑缝章和印章（SignComponents中有两个Component元素，骑缝章（SIGN_PAGING_SEAL）采用绝对定位，即指定具体的ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage方式；印章（SIGN_SEAL）使用表单域定位方式，即GenerateMode = FIELD）。
3. 他方企业参与者仅具有一个印章签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SEAL，使用表单域定位方式，即GenerateMode = FIELD）。
4. C端参与者仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，使用表单域定位方式，即GenerateMode = FIELD）。
5. 本合同为有序签署（Unordered传递为false或不传递）。
6. 有关表单域PDF的创建方式，请参阅电子签开发者中心 -> 常见问题 -> PDF相关介绍。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName B2B2C表单域有序签署示例合同 \
    --FlowType 示例合同 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.PreReadTime 10 \
    --Approvers.0.SignComponents.0.GenerateMode FIELD \
    --Approvers.0.SignComponents.0.ComponentName seal \
    --Approvers.0.SignComponents.0.ComponentHeight 0 \
    --Approvers.0.SignComponents.0.ComponentWidth 0 \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 0 \
    --Approvers.0.SignComponents.0.ComponentPosY 0 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.1.ComponentPosX 160 \
    --Approvers.0.SignComponents.1.ComponentPosY 260 \
    --Approvers.0.SignComponents.1.ComponentWidth 100 \
    --Approvers.0.SignComponents.1.FileIndex 0 \
    --Approvers.0.SignComponents.1.ComponentType SIGN_PAGING_SEAL \
    --Approvers.0.SignComponents.1.ComponentPage 1 \
    --Approvers.0.SignComponents.1.ComponentHeight 100 \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 张三示例企业 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.PreReadTime 10 \
    --Approvers.1.SignComponents.0.ComponentHeight 0 \
    --Approvers.1.SignComponents.0.ComponentWidth 0 \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 0 \
    --Approvers.1.SignComponents.0.ComponentPosY 0 \
    --Approvers.1.SignComponents.0.GenerateMode FIELD \
    --Approvers.1.SignComponents.0.ComponentName seal2 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.2.ApproverType 1 \
    --Approvers.2.NotifyType NONE \
    --Approvers.2.ApproverName 李四 \
    --Approvers.2.ApproverMobile 15100000000 \
    --Approvers.2.PreReadTime 10 \
    --Approvers.2.SignComponents.0.ComponentHeight 0 \
    --Approvers.2.SignComponents.0.ComponentWidth 0 \
    --Approvers.2.SignComponents.0.ComponentPage 1 \
    --Approvers.2.SignComponents.0.ComponentPosX 0 \
    --Approvers.2.SignComponents.0.ComponentPosY 0 \
    --Approvers.2.SignComponents.0.GenerateMode FIELD \
    --Approvers.2.SignComponents.0.ComponentName signature \
    --Approvers.2.SignComponents.0.FileIndex 0 \
    --Approvers.2.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk
```

Output: 
```
{
    "Response": {
        "FlowId": "yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 5: 创建一份涉及本方企业自动签署和个人签署的B2C合同**

1. 签署方包括本方企业和个人（在Approvers中包含两个ApproverInfo元素）。
2. 本方企业采用自动签署方式（在approver中将approverType设置为3）。
3. 在发起合同之前，需要为本方经办人开通并授权自动签署功能（登录腾讯电子签控制台 -> 更多能力 -> 企业设置 -> 拓展服务 -> 企业自动签署），详见<a href="https://qian.tencent.com/document/92776/">企业自动签署开通参考文档</a>
4. 自动签署方的签署人默认为发起方。
5. 本方企业的签署区仅包含一个印章签署控件：印章（在SignComponents中包含一个Component元素，印章（SIGN_SEAL）采用绝对定位方式，即指定具体的ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage）。
6. 本方企业的印章控件必须指定印章（ComponentValue必须指定当前员工已经授权的印章Id，可登录腾讯电子签控制台 -> 印章 -> 印章中心 选择某一个印章，在页面上显示为印章ID）。
7. C端参与者仅包含一个签名签署控件（在SignComponents中仅包含一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，采用绝对定位方式，即指定具体的ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage）。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 静默签署 & B2C合同 \
    --FlowType 示例合同 \
    --Approvers.0.ApproverType 3 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.PreReadTime 10 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentValue yDxMjUyKQDN7EkUuO4zjEBpGXvHEACSA \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 15100000000 \
    --Approvers.1.PreReadTime 10 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 160 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FileIds yDwqYUUckp39gkfxUu14JJPxaTyM1ltq
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwqoUUckp3bkzgpUuPTimaSDVz2ukqv",
        "PreviewUrl": "",
        "RequestId": "s1692183667030779528"
    }
}
```

**Example 6: 创建一份签署方拖拽签署区域的合同**

1. 签署方包括本方企业、他方企业和个人（Approvers中有三个ApproverInfo元素）。
2. 所有签署方企业都不包允许有签署控件。
3. 设置当前流程为可拖拽（SignBeanTag）。
4. 本合同为无序签署（Unordered传递为true）。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Unordered True \
    --FlowName 签署时拖拽签署控件合同 \
    --SignBeanTag 1 \
    --FlowType 示例合同 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.PreReadTime 10 \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 张三示例企业 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.PreReadTime 10 \
    --Approvers.2.ApproverType 1 \
    --Approvers.2.NotifyType NONE \
    --Approvers.2.ApproverName 李四 \
    --Approvers.2.ApproverMobile 15100000000 \
    --Approvers.2.PreReadTime 10 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwqoUUckp3bkmc7UuPTimaxVoB5m1iD",
        "PreviewUrl": "",
        "RequestId": "s1692184714668577966"
    }
}
```

**Example 7: 创建仅有个人C端签署的合同，进行预览，不发起**

1. 只有一个个人C端参与人（Approvers中仅有一个ApproverInfo元素）。
2. 发起时，配置两个发起方填写文本控件（Components中Component元素Type为Text，并使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
3. 通过绝对定位指定签署区（SignComponents中Component元素指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
4. C端参与人仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE）。
5. 文件发起时，设置NeedPreview为1，当PreviewType设置为1时，以文件链接方式返回预览链接（即打开链接会自动进行下载）。
6. 仅返回预览链接，不返回合同ID（flowId），仅用于预览。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Unordered True \
    --Components.0.ComponentPosY 260 \
    --Components.0.ComponentWidth 100 \
    --Components.0.FileIndex 0 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentValue 典子谦 \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 160 \
    --Components.0.ComponentHeight 100 \
    --Components.1.ComponentPosY 360 \
    --Components.1.ComponentWidth 100 \
    --Components.1.FileIndex 0 \
    --Components.1.ComponentType TEXT \
    --Components.1.ComponentValue 典子谦 \
    --Components.1.ComponentPage 1 \
    --Components.1.ComponentPosX 160 \
    --Components.1.ComponentHeight 100 \
    --FlowName 单C合同预览 \
    --FlowType 示例合同 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk \
    --NeedPreview True \
    --PreviewType 1
```

Output: 
```
{
    "Response": {
        "FlowId": "",
        "PreviewUrl": "https://test.ess.tencent.cn/document-url-preview?channel=PROXYCHANNEL&scene=SINGLEPAGE&code=yDwqoUUckp3bkmmlUuPTimaSa2YKny&codeType=QUICK&businessType=RESOURCE&businessId=yDwqcUUckp39ix54URyS6kCwo8MdKEon",
        "RequestId": "s1692272754129210855"
    }
}
```

**Example 8: 创建只有个人C端签署, 签署人需要人脸校验认证的合同流程 **

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

**Example 9: 处方单场景**

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

**Example 10: 集团企业代表子公司创建仅具有个人C端签署的合同流程，签署人可选择人脸验证、密码验证或短信验证码验证**

1. 只有一个个人C端参与者（Approvers中仅有一个ApproverInfo元素）。
2. 通过绝对定位来指定签署区域（SignComponents中的Component元素指定具体的ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage方式）。
3. C端参与者只有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE）。
4. C端签署人需进行人脸验证以签署合同（将ApproverSignTypes属性设置为[1,2,3]，表示可选择人脸识别验证、密码验证或短信验证码验证来签署合同）。
5. 集团企业代表子公司发送合同（在agent中，将ProxyOrganizationId设置为子公司的organizationId，可在腾讯系电子签登录后的组织管理 -> 集团组织管理 -> 成员企业列表中找到企业id）。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Agent.ProxyOrganizationId yDwFdUUckpsvm3ciUyVYxhuSAkZziLk7 \
    --FlowName 主代子单个个人签署方合同示例 \
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
    --Approvers.0.SignComponents.1.ComponentPosX 160 \
    --Approvers.0.SignComponents.1.ComponentPosY 360 \
    --Approvers.0.SignComponents.1.ComponentWidth 50 \
    --Approvers.0.SignComponents.1.ComponentHeight 50 \
    --Approvers.0.SignComponents.1.FileIndex 0 \
    --Approvers.0.SignComponents.1.ComponentType SIGN_DATE \
    --Approvers.0.SignComponents.1.ComponentPage 1 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk
```

Output: 
```
{
    "Response": {
        "FlowId": "yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 11: 发起合同后添加签署区-指定签署控件和印章的无序签署示例合同**

1. 签署方包括本方企业、他方企业和个人（Approvers中有三个ApproverInfo元素）。
2. 允许签署方在签署时自行添加签署控件，可以拖动位置和控制数量。（SignBeanTag 设置为1）
3. 明确规定本方企业在签署时可以添加骑缝章控件（SIGN_PAGING_SEAL）、印章控件（SIGN_SEAL）、和法人控件（SIGN_LEGAL_PERSON_SEAL），并且限制了骑缝章控件和印章控件可用的印章ID列表。
4. 明确规定他方企业在签署时必须使用印章控件（SIGN_SEAL）。
5. 明确规定个人签署方在签署时必须使用签名控件（SIGN_SIGNATURE），并且使用系统签名（SYSTEM_ESIGN）。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 发起合同后添加签署区-指定签署控件和印章的无序签署示例合同 \
    --FlowType 示例合同 \
    --Unordered True \
    --SignBeanTag 1 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.PreReadTime 10 \
    --Approvers.0.AddSignComponentsLimits.0.ComponentType SIGN_SEAL \
    --Approvers.0.AddSignComponentsLimits.0.ComponentValue yDwJCUUckpk7t9yyUuXF6wL8KMm3yXcX yDRRuUUgygjvznc7UuO5sjES5RaqSnyn \
    --Approvers.0.AddSignComponentsLimits.1.ComponentType SIGN_PAGING_SEAL \
    --Approvers.0.AddSignComponentsLimits.1.ComponentValue yDwJCUUckpk7t9yyUuXF6wL8KMm3yXcX yDRRuUU2qyjvspleUuO6zjE1EkGzMK1A \
    --Approvers.0.AddSignComponentsLimits.2.ComponentType SIGN_LEGAL_PERSON_SEAL \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 张三示例企业 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.PreReadTime 10 \
    --Approvers.1.AddSignComponentsLimits.0.ComponentType SIGN_SEAL \
    --Approvers.2.ApproverType 1 \
    --Approvers.2.ApproverName 李四 \
    --Approvers.2.ApproverMobile 15100000000 \
    --Approvers.2.PreReadTime 10 \
    --Approvers.2.AddSignComponentsLimits.0.ComponentType SIGN_SIGNATURE \
    --Approvers.2.AddSignComponentsLimits.0.ComponentValue SYSTEM_ESIGN \
    --FileIds yDwqYUUckp93gkfxUu14JJPxaTy13dtq
```

Output: 
```
{
    "Response": {
        "FlowId": "yDJJPxaTy13dtqwqYUUckp93gkfxUu14",
        "PreviewUrl": "",
        "RequestId": "s1674414304627348115"
    }
}
```

**Example 12: 标书场景下，需要创建一份本方企业和个人签署的标书文件，要求本方企业的印章控件需要在每一页都进行盖章。**

1. 签署方包括本方企业和个人（Approvers中有两个ApproverInfo元素）。
2. 本方企业的签署区仅具有一个印章签署控件：印章（SignComponents中有一个Component元素，印章（SIGN_SEAL）使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
3. 本方企业的印章签署区需要在所有的页面上面进行加盖，即设置"ComponentExtra":"{\"PageRanges\":[{\"BeginPage\":1,\"EndPage\":-1}]}",
4. C端参与者仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 标书文件合同示例 \
    --FlowType 示例合同 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.SignComponents.0.ComponentPosY 360 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 60 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.ComponentExtra {"PageRanges":[{"BeginPage":1,"EndPage":-1}]} \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 160 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwFkUUckpstin4sUuZjBEY5Ia2XB7sz",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

