**Example 1: 处方单场景**

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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo432UunP4DaCo2sOe2oP",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo43jUunP4DaSlfnawIyd",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDRsDUUgyg1aczxtUuNAW8Cx4WsAiEB5",
        "PreviewUrl": "",
        "RequestId": "43b9474a-c909-4d89-aa7b-3632f02fa8a4"
    }
}
```

**Example 2: 创建一份签署方拖拽签署区域的合同**

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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmtvyqURxlqRxRRQF8HT1m",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmtvyhURxlqRxSEfd0ag4h",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmt1ffUm8eW6u0kLIxrZpw",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDwqoUUckp3bkmc7UuPTimaxVoB5m1iD",
        "PreviewUrl": "",
        "RequestId": "s1692184714668577966"
    }
}
```

**Example 3: 创建一份本方企业和个人进行签署合同**

1. 签署方包括本方企业和个人（Approvers中有两个ApproverInfo元素）。
2. 本方企业签署前需要审核（将NeedSignReview设置为true）。
3. 本方企业的签署区仅具有一个印章签署控件：印章（SignComponents中有一个Component元素，印章（SIGN_SEAL）使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
4. C端参与者仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，使用绝对定位方式，即指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式）。
5. 本流程包含两个抄送人，抄送人可查看合同信息（CcInfos中有两个CcInfo的信息）。
6. 指定每个签署方的角色名称。

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
    --Approvers.0.ApproverRoleName 甲方 \
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
    --Approvers.1.ApproverRoleName 乙方 \
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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmt1u6Um8eW68pzwLGTld6",
                "ApproverRoleName": "甲方"
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmt1uzUm8eW6CchGlBHFwy",
                "ApproverRoleName": "乙方"
            }
        ],
        "FlowId": "yDwqoUUckp3bkmc7UuPTimaxVoB5m1iD",
        "PreviewUrl": "",
        "RequestId": "s1692184714668577966"
    }
}
```

**Example 4: 通过文件发起B2C合同-控件使用绝对定位方式**

1.通过PDF文件发起合同
2.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】
3.通过绝对对位方式指定【典子谦示例企业】的签署控件为印章控件，控件位置为该文件的第1页，横坐标160，纵坐标260的位置，控件高宽为119x119（公章大小）
4.指定C端签署方为个人【李四】，联系电话为【15100000000】
5.通过绝对对位方式指定【李四】的签署控件为手写签名控件，控件位置为该文件的第1页，横坐标60，纵坐标260的位置，控件高宽为119x43（推荐的手写签名大小）
6.通过绝对定位方式在合同文件的第1页，横坐标360，纵坐标360的位置放置一个单行文本控件，并写入内容【我是一个单行文本】
7.完成合同发起

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 通过文件发起合同 \
    --FlowDescription 通过文件发起合同 \
    --Unordered False \
    --FlowType 示例合同 \
    --Deadline 1830268800 \
    --SignBeanTag 1 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.ApproverIdCardType  \
    --Approvers.0.ApproverIdCardNumber  \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentHeight 119 \
    --Approvers.0.SignComponents.0.ComponentWidth 119 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentValue  \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 15100000000 \
    --Approvers.1.PreReadTime 10 \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 60 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 119 \
    --Approvers.1.SignComponents.0.ComponentHeight 43 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FileIds yDwqYUUckp39gkfxUu14JJPxaTyM1ltq \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 360 \
    --Components.0.ComponentPosY 360 \
    --Components.0.ComponentWidth 100 \
    --Components.0.ComponentHeight 100 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentValue 我是一个单行文本 \
    --Components.0.FileIndex 0
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo432UunP4DaCo2sOe2oP",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 5: 通过文件发起B2C合同-控件使用关键字定位方式**

1.通过PDF文件发起合同
2.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】
3.通过绝对对位方式指定【典子谦示例企业】的签署控件为印章控件，控件类型为【KEYWORD】关键字类型，并设置关键字为【签名】，关键字查找顺序为【Positive-正序】关键字位置模式为【Middle-居中】，控件高宽为119x119（公章大小）
4.指定C端签署方为个人【李四】，联系电话为【15100000000】
5.通过绝对对位方式指定【李四】的签署控件为手写签名控件，控件位置为该文件的第1页，横坐标60，纵坐标260的位置，控件高宽为119x43（推荐的手写签名大小）
6.通过绝对定位方式在合同文件的第1页，横坐标360，纵坐标360的位置放置一个单行文本控件，并写入内容【我是一个单行文本】
7.完成合同发起

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --FlowName 通过文件发起合同-关键字定位 \
    --FlowDescription 通过文件发起合同 \
    --Unordered False \
    --FlowType 示例合同 \
    --Deadline 1830268800 \
    --SignBeanTag 1 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.ApproverIdCardType  \
    --Approvers.0.ApproverIdCardNumber  \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 0 \
    --Approvers.0.SignComponents.0.ComponentPosY 0 \
    --Approvers.0.SignComponents.0.ComponentWidth 119 \
    --Approvers.0.SignComponents.0.ComponentHeight 119 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.GenerateMode KEYWORD \
    --Approvers.0.SignComponents.0.ComponentId 签名 \
    --Approvers.0.SignComponents.0.KeywordOrder Positive \
    --Approvers.0.SignComponents.0.RelativeLocation Middle \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 15100000000 \
    --Approvers.1.PreReadTime 10 \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 60 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 119 \
    --Approvers.1.SignComponents.0.ComponentHeight 43 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FileIds yDwqYUUckp39gkfxUu14JJPxaTyM1ltq \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 360 \
    --Components.0.ComponentPosY 360 \
    --Components.0.ComponentWidth 100 \
    --Components.0.ComponentHeight 100 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentValue 我是一个单行文本 \
    --Components.0.FileIndex 0
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo432UunP4DaCo2sOe2oP",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 6: 创建仅有个人C端签署的合同，进行预览，不发起**

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

**Example 7: 文件发起B2C合同，签署双方和发起方都有填写控件**

1.通过PDF文件发起合同
2.指定B端签署方为企业【典子谦示例企业】，经办人为【何规】
3.指定C端签署方为个人【张三】
4.发起方填写控件为通过外层 参数 Components 传递，需要在发起时通过 ComponentValue 指定值
5.签署方填写控件通过Approvers.Components传递，在发起时不能通过 ComponentValue 指定值，需要签署人在合同成功发起后自己填写
6.更多签署方填写控件示例 可参考文档 [指定签署方填写控件](https://qian.tencent.com/developers/company/createFlowByFiles#%E6%8C%87%E5%AE%9A%E7%AD%BE%E7%BD%B2%E6%96%B9%E5%A1%AB%E5%86%99%E6%8E%A7%E4%BB%B6)

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId yDxbTUyKQWPt5NUuO4zjEuyFAyOX3v9C \
    --FlowName 文件发起B2C-签署人带填写控件 \
    --Components.0.ComponentHeight 20 \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 205 \
    --Components.0.ComponentPosY 90 \
    --Components.0.ComponentValue （落霞与孤鹜齐飞，秋水共长天一色）这是发起方填写的文本 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentWidth 339 \
    --Components.0.FileIndex 0 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.ApproverName 何规 \
    --Approvers.0.ApproverMobile 18200000000 \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.SignComponents.0.ComponentHeight 119 \
    --Approvers.0.SignComponents.0.ComponentPage 7 \
    --Approvers.0.SignComponents.0.ComponentPosX 143.59375 \
    --Approvers.0.SignComponents.0.ComponentPosY 169.0625 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentWidth 119 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.Components.0.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-CREDIT-CODE","FontColor":"0,82,217"} \
    --Approvers.0.Components.0.ComponentHeight 20 \
    --Approvers.0.Components.0.ComponentPage 1 \
    --Approvers.0.Components.0.ComponentPosX 205 \
    --Approvers.0.Components.0.ComponentPosY 114 \
    --Approvers.0.Components.0.ComponentRequired True \
    --Approvers.0.Components.0.ComponentType TEXT \
    --Approvers.0.Components.0.ComponentWidth 339 \
    --Approvers.0.Components.0.FileIndex 0 \
    --Approvers.0.Components.1.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-CREDIT-CODE"} \
    --Approvers.0.Components.1.ComponentHeight 20 \
    --Approvers.0.Components.1.ComponentPage 1 \
    --Approvers.0.Components.1.ComponentPosX 234 \
    --Approvers.0.Components.1.ComponentPosY 142 \
    --Approvers.0.Components.1.ComponentRequired True \
    --Approvers.0.Components.1.ComponentType TEXT \
    --Approvers.0.Components.1.ComponentWidth 302 \
    --Approvers.0.Components.1.FileIndex 0 \
    --Approvers.0.Components.2.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-LEGAL-NAME"} \
    --Approvers.0.Components.2.ComponentHeight 20 \
    --Approvers.0.Components.2.ComponentPage 1 \
    --Approvers.0.Components.2.ComponentPosX 191.09 \
    --Approvers.0.Components.2.ComponentPosY 172 \
    --Approvers.0.Components.2.ComponentRequired True \
    --Approvers.0.Components.2.ComponentType TEXT \
    --Approvers.0.Components.2.ComponentWidth 335 \
    --Approvers.0.Components.2.FileIndex 0 \
    --Approvers.0.Components.3.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --Approvers.0.Components.3.ComponentHeight 21 \
    --Approvers.0.Components.3.ComponentPage 1 \
    --Approvers.0.Components.3.ComponentPosX 155 \
    --Approvers.0.Components.3.ComponentPosY 205 \
    --Approvers.0.Components.3.ComponentRequired True \
    --Approvers.0.Components.3.ComponentType MULTI_LINE_TEXT \
    --Approvers.0.Components.3.ComponentWidth 366 \
    --Approvers.0.Components.3.FileIndex 0 \
    --Approvers.0.Components.4.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-NAME"} \
    --Approvers.0.Components.4.ComponentHeight 20 \
    --Approvers.0.Components.4.ComponentPage 1 \
    --Approvers.0.Components.4.ComponentPosX 107 \
    --Approvers.0.Components.4.ComponentPosY 236 \
    --Approvers.0.Components.4.ComponentRequired True \
    --Approvers.0.Components.4.ComponentType TEXT \
    --Approvers.0.Components.4.ComponentWidth 339 \
    --Approvers.0.Components.4.FileIndex 0 \
    --Approvers.0.Components.5.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-MOBILE"} \
    --Approvers.0.Components.5.ComponentHeight 20 \
    --Approvers.0.Components.5.ComponentPage 1 \
    --Approvers.0.Components.5.ComponentPosX 121 \
    --Approvers.0.Components.5.ComponentPosY 265 \
    --Approvers.0.Components.5.ComponentRequired True \
    --Approvers.0.Components.5.ComponentType TEXT \
    --Approvers.0.Components.5.ComponentWidth 327 \
    --Approvers.0.Components.5.FileIndex 0 \
    --Approvers.0.Components.6.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --Approvers.0.Components.6.ComponentHeight 20 \
    --Approvers.0.Components.6.ComponentPage 1 \
    --Approvers.0.Components.6.ComponentPosX 35.09 \
    --Approvers.0.Components.6.ComponentPosY 293 \
    --Approvers.0.Components.6.ComponentRequired True \
    --Approvers.0.Components.6.ComponentType DISTRICT \
    --Approvers.0.Components.6.ComponentWidth 306 \
    --Approvers.0.Components.6.FileIndex 0 \
    --Approvers.0.Components.7.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --Approvers.0.Components.7.ComponentHeight 44 \
    --Approvers.0.Components.7.ComponentPage 1 \
    --Approvers.0.Components.7.ComponentPosX 44 \
    --Approvers.0.Components.7.ComponentPosY 652 \
    --Approvers.0.Components.7.ComponentType MULTI_LINE_TEXT \
    --Approvers.0.Components.7.ComponentWidth 505 \
    --Approvers.0.Components.7.FileIndex 0 \
    --Approvers.0.Components.8.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","ManualFill":true} \
    --Approvers.0.Components.8.ComponentHeight 20 \
    --Approvers.0.Components.8.ComponentPage 2 \
    --Approvers.0.Components.8.ComponentPosX 145 \
    --Approvers.0.Components.8.ComponentPosY 68 \
    --Approvers.0.Components.8.ComponentRequired True \
    --Approvers.0.Components.8.ComponentType DATE \
    --Approvers.0.Components.8.ComponentWidth 116 \
    --Approvers.0.Components.8.FileIndex 0 \
    --Approvers.0.Components.9.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","ManualFill":true} \
    --Approvers.0.Components.9.ComponentHeight 20 \
    --Approvers.0.Components.9.ComponentPage 2 \
    --Approvers.0.Components.9.ComponentPosX 130.09375 \
    --Approvers.0.Components.9.ComponentPosY 555.09375 \
    --Approvers.0.Components.9.ComponentType DATE \
    --Approvers.0.Components.9.ComponentWidth 116 \
    --Approvers.0.Components.9.FileIndex 0 \
    --Approvers.0.Components.10.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --Approvers.0.Components.10.ComponentHeight 27 \
    --Approvers.0.Components.10.ComponentPage 2 \
    --Approvers.0.Components.10.ComponentPosX 134.09 \
    --Approvers.0.Components.10.ComponentPosY 628.09 \
    --Approvers.0.Components.10.ComponentType MULTI_LINE_TEXT \
    --Approvers.0.Components.10.ComponentWidth 398 \
    --Approvers.0.Components.10.FileIndex 0 \
    --Approvers.0.Components.11.ComponentExtra {} \
    --Approvers.0.Components.11.ComponentHeight 16 \
    --Approvers.0.Components.11.ComponentPage 7 \
    --Approvers.0.Components.11.ComponentPosX 83.09375 \
    --Approvers.0.Components.11.ComponentPosY 96.5625 \
    --Approvers.0.Components.11.ComponentType CHECK_BOX \
    --Approvers.0.Components.11.ComponentWidth 16 \
    --Approvers.0.Components.11.FileIndex 0 \
    --Approvers.0.Components.12.ComponentExtra {"FillMethod":0,"NotMakeImageCenter":true} \
    --Approvers.0.Components.12.ComponentHeight 119 \
    --Approvers.0.Components.12.ComponentPage 7 \
    --Approvers.0.Components.12.ComponentPosX 13 \
    --Approvers.0.Components.12.ComponentPosY 394 \
    --Approvers.0.Components.12.ComponentType FILL_IMAGE \
    --Approvers.0.Components.12.ComponentWidth 119 \
    --Approvers.0.Components.12.FileIndex 0 \
    --Approvers.0.Components.13.ComponentExtra {"LimitCount":3,"AttachmentType":"IMG"} \
    --Approvers.0.Components.13.ComponentHeight 42 \
    --Approvers.0.Components.13.ComponentPage 7 \
    --Approvers.0.Components.13.ComponentPosX 12 \
    --Approvers.0.Components.13.ComponentPosY 537 \
    --Approvers.0.Components.13.ComponentRequired True \
    --Approvers.0.Components.13.ComponentType ATTACHMENT \
    --Approvers.0.Components.13.ComponentWidth 240 \
    --Approvers.0.Components.13.FileIndex 0 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18700000000 \
    --Approvers.1.NotifyType NONE \
    --Approvers.1.SignComponents.0.ComponentHeight 43 \
    --Approvers.1.SignComponents.0.ComponentPage 7 \
    --Approvers.1.SignComponents.0.ComponentPosX 433.59375 \
    --Approvers.1.SignComponents.0.ComponentPosY 196.0625 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentWidth 119 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.Components.0.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-NAME"} \
    --Approvers.1.Components.0.ComponentHeight 20 \
    --Approvers.1.Components.0.ComponentPage 1 \
    --Approvers.1.Components.0.ComponentPosX 199 \
    --Approvers.1.Components.0.ComponentPosY 323 \
    --Approvers.1.Components.0.ComponentRequired True \
    --Approvers.1.Components.0.ComponentType TEXT \
    --Approvers.1.Components.0.ComponentWidth 309 \
    --Approvers.1.Components.0.FileIndex 0 \
    --Approvers.1.Components.1.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --Approvers.1.Components.1.ComponentHeight 24 \
    --Approvers.1.Components.1.ComponentPage 1 \
    --Approvers.1.Components.1.ComponentPosX 155 \
    --Approvers.1.Components.1.ComponentPosY 386 \
    --Approvers.1.Components.1.ComponentRequired True \
    --Approvers.1.Components.1.ComponentType MULTI_LINE_TEXT \
    --Approvers.1.Components.1.ComponentWidth 390 \
    --Approvers.1.Components.1.FileIndex 0 \
    --Approvers.1.Components.2.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --Approvers.1.Components.2.ComponentHeight 20 \
    --Approvers.1.Components.2.ComponentPage 1 \
    --Approvers.1.Components.2.ComponentPosX 114.09 \
    --Approvers.1.Components.2.ComponentPosY 416 \
    --Approvers.1.Components.2.ComponentRequired True \
    --Approvers.1.Components.2.ComponentType TEXT \
    --Approvers.1.Components.2.ComponentWidth 299 \
    --Approvers.1.Components.2.FileIndex 0 \
    --Approvers.1.Components.3.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-MOBILE"} \
    --Approvers.1.Components.3.ComponentHeight 20 \
    --Approvers.1.Components.3.ComponentPage 1 \
    --Approvers.1.Components.3.ComponentPosX 115.09 \
    --Approvers.1.Components.3.ComponentPosY 445 \
    --Approvers.1.Components.3.ComponentRequired True \
    --Approvers.1.Components.3.ComponentType TEXT \
    --Approvers.1.Components.3.ComponentWidth 367 \
    --Approvers.1.Components.3.FileIndex 0 \
    --Approvers.1.Components.4.ComponentExtra {"SubType":"EDUCATION"} \
    --Approvers.1.Components.4.ComponentHeight 20 \
    --Approvers.1.Components.4.ComponentId ComponentId_30 \
    --Approvers.1.Components.4.ComponentName 学历 \
    --Approvers.1.Components.4.ComponentPage 1 \
    --Approvers.1.Components.4.ComponentPosX 8.09375 \
    --Approvers.1.Components.4.ComponentPosY 473 \
    --Approvers.1.Components.4.ComponentRequired True \
    --Approvers.1.Components.4.ComponentType SELECTOR \
    --Approvers.1.Components.4.ComponentWidth 84 \
    --Approvers.1.Components.4.FileIndex 0 \
    --Approvers.1.Components.5.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"EMAIL"} \
    --Approvers.1.Components.5.ComponentHeight 20 \
    --Approvers.1.Components.5.ComponentId ComponentId_28 \
    --Approvers.1.Components.5.ComponentName 邮箱 \
    --Approvers.1.Components.5.ComponentPage 1 \
    --Approvers.1.Components.5.ComponentPosX 117.09375 \
    --Approvers.1.Components.5.ComponentPosY 474 \
    --Approvers.1.Components.5.ComponentType TEXT \
    --Approvers.1.Components.5.ComponentWidth 292 \
    --Approvers.1.Components.5.FileIndex 0 \
    --Approvers.1.Components.6.ComponentExtra {"SubType":"GENDER"} \
    --Approvers.1.Components.6.ComponentHeight 20 \
    --Approvers.1.Components.6.ComponentId ComponentId_29 \
    --Approvers.1.Components.6.ComponentName 性别 \
    --Approvers.1.Components.6.ComponentPage 1 \
    --Approvers.1.Components.6.ComponentPosX 424.09375 \
    --Approvers.1.Components.6.ComponentPosY 472 \
    --Approvers.1.Components.6.ComponentRequired True \
    --Approvers.1.Components.6.ComponentType SELECTOR \
    --Approvers.1.Components.6.ComponentWidth 84 \
    --Approvers.1.Components.6.FileIndex 0 \
    --FileIds yDCWqUUckpve5id3U4f5EL77tlNh6zTZ
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCVsUUckpwri2v6U9JHnkxcJrDXddLQ",
                "SignId": "yDCVsUUckpwri3vwU9JHnky9uvwe3h25"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCVsUUckpwri2vbU9JHnkSdZKiAyEs3",
                "SignId": "yDCVsUUckpwri2vvU9JHnkvaHtOttw1h"
            }
        ],
        "FlowId": "yDCVsUUckpwri3vyU9JHnkBDqTFanBa3",
        "PreviewUrl": "",
        "RequestId": "s1709793654575755487"
    }
}
```

**Example 8: 创建一份涉及本方企业自动签署和个人签署的B2C合同**

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

**Example 9: 创建含有动态签署人流程，签署方不指定具体的签署人**

创建一个B2C流程，两方签署方不指定具体的签署人
注：
`1.签署人相关信息为空，如：姓名、手机号码等`
`2.FillType需传值为1，表示为动态签署人（不确定具体的签署人），需后续进行补充。`
`3.需保留对应的角色编号，即RecipientId，后续补充具体的签署人时需指定对应的RecipientId`

Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 19561039c99fe825a934a132520fde6a \
    --Agent.ProxyOrganizationId yDwFdUUckpsvm3ciUyVYxhuSAkZziLk7 \
    --FlowName 发起动态签署人合同示例 \
    --FlowType 合同 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.ApproverName  \
    --Approvers.0.ApproverMobile  \
    --Approvers.0.NotifyType NONE \
    --Approvers.0.ApproverSignTypes 1 \
    --Approvers.0.ApproverRoleName 甲方 \
    --Approvers.0.ApproverOption.FillType 1 \
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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo432UunP4DaCo2sOe2oP",
                "ApproverRoleName": "甲方"
            }
        ],
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 10: 创建只有个人C端签署, 签署人需要人脸校验认证的合同流程 **

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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo432UunP4DaCo2sOe2oP",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDRsDUUgyg1aczxtUuNAW8Cx4WsAiEB5",
        "PreviewUrl": "",
        "RequestId": "43b9474a-c909-4d89-aa7b-3632f02fa8a4"
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

**Example 12: 创建一份涉及本方企业、他方企业和个人签署的三方无序签署合同**

1. 签署方包括本方企业、他方企业和个人（Approvers中有三个ApproverInfo元素）。
2. 本方企业的签署区仅具有一个印章签署控件：印章（SignComponents中有一个Component元素，印章（SIGN_SEAL）使用关键字定位方式，即GenerateMode = KEYWORD）。
3. 他方企业参与者仅具有一个印章签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SEAL，使用关键字定位方式，即GenerateMode = KEYWORD）。
4. C端参与者仅具有一个签名签署控件（SignComponents中仅有一个Component元素，且该元素的ComponentType为SIGN_SIGNATURE，使用关键字定位方式，即GenerateMode = KEYWORD）。
5. 本合同为无序签署（Unordered传递为true）。
6. 关键字定位PDF的创建方式，请参阅电子签开发者中心 -> 常见问题 -> PDF相关介绍。

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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmtv3xURxlqRxuNInLC9Kh",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmtv3uURxlqRxxIBOdNTfT",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmt17kUm8eW6SG8c7HRoJR",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDwqoUUckp3bkmmbUuPTimaq7zNEvxoX",
        "PreviewUrl": "",
        "RequestId": "s1692265794625568498"
    }
}
```

**Example 13: 创建一份涉及本方企业、他方企业和个人签署的三方有序签署合同**

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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmtvt0URxlqRxSQ0CRRaG8",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmtvtgURxlqRxyACZnBnZq",
                "ApproverRoleName": ""
            },
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmt19bUm8eW68mThldYiee",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 14: 错误示例：签署人姓名格式传递错误，导致合同创建失败，不扣费用。**

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

**Example 15: 集团企业代表子公司创建仅具有个人C端签署的合同流程，签署人可选择人脸验证、密码验证或短信验证码验证**

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
        "Approvers": [
            {
                "SignId": "",
                "RecipientId": "yDw7hUUckpkmo432UunP4DaCo2sOe2oP",
                "ApproverRoleName": ""
            }
        ],
        "FlowId": "yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS",
        "PreviewUrl": "",
        "RequestId": "s1665674603446404796"
    }
}
```

**Example 16: 标书场景下，需要创建一份本方企业和个人签署的标书文件，要求本方企业的印章控件需要在每一页都进行盖章。**

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

