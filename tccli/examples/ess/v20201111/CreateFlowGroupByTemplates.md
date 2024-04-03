**Example 1: 错误示例：签署人姓名格式传递错误，导致合同组创建失败**

1.子合同2的签署人姓名填写非法，导致合同组发起失败
2.合同组合同要么全部发起成功，要么全部失败，不会存在部分成功场景

Input: 

```
tccli ess CreateFlowGroupByTemplates --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowGroupName 示例合同组-有2份子合同 \
    --FlowGroupOptions.ApproverVerifyType MobileCheck \
    --FlowGroupOptions.SelfOrganizationApproverNotifyType none \
    --FlowGroupOptions.OtherApproverNotifyType sms \
    --FlowGroupInfos.0.TemplateId yDwXhUUckp7fs563UyNzLyWRHKWco8JV \
    --FlowGroupInfos.0.FlowName 子合同1-B2C \
    --FlowGroupInfos.0.Components.0.ComponentName 单行文本 \
    --FlowGroupInfos.0.Components.0.ComponentValue 单行文本测试 \
    --FlowGroupInfos.0.Components.0.ComponentType TEXT \
    --FlowGroupInfos.0.Components.0.FileIndex 0 \
    --FlowGroupInfos.0.Components.0.ComponentHeight 0 \
    --FlowGroupInfos.0.Components.0.ComponentWidth 0 \
    --FlowGroupInfos.0.Components.0.ComponentPage 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosX 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosY 0 \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.TemplateId yDwJ4UUckpk84g04UyPWcjIEMPGLGe2z \
    --FlowGroupInfos.1.FlowName 子合同2 \
    --FlowGroupInfos.1.FlowDescription 子合同2-B2B \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 典子谦&&& \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Unordered True
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.Name",
            "Message": "参数错误,名字`典子谦&&&`填写错误,请修改后重试"
        },
        "RequestId": "s1694674067353270559"
    }
}
```

**Example 2: 创建一个有两份子合同的合同组签署流程（B2B、B2C（B端自动签署））**

1. 子合同1为B2C合同，Approvers中包含两个ApproverInfo元素，C端签署人ApproverType为1，企业签署人ApproverType为3，表示B端自动签署。

2. 子合同1使用模板yDwXhUUckp7fs563UyNzLyWRHKWco8JV发起B端自动签署合同。需要确保在创建模板时，模板中已经指定了本企业的印章控件，否则合同发起将会失败。

3. 子合同2为B2B合同，Approvers中包含两个ApproverInfo元素，企业签署人ApproverType为0。

Input: 

```
tccli ess CreateFlowGroupByTemplates --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowGroupName 示例合同组-有2份子合同 \
    --FlowGroupInfos.0.TemplateId yDwXhUUckp7fs563UyNzLyWRHKWco8JV \
    --FlowGroupInfos.0.FlowName 子合同1-B2C \
    --FlowGroupInfos.0.Components.0.ComponentName 单行文本 \
    --FlowGroupInfos.0.Components.0.ComponentValue 单行文本测试 \
    --FlowGroupInfos.0.Components.0.ComponentType TEXT \
    --FlowGroupInfos.0.Components.0.FileIndex 0 \
    --FlowGroupInfos.0.Components.0.ComponentHeight 0 \
    --FlowGroupInfos.0.Components.0.ComponentWidth 0 \
    --FlowGroupInfos.0.Components.0.ComponentPage 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosX 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosY 0 \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 3 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.TemplateId yDwJ5UUckpk84g04UyPWcjIEMPGLGe3z \
    --FlowGroupInfos.1.FlowName 子合同2 \
    --FlowGroupInfos.1.FlowDescription 子合同2-B2B \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Unordered True
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwJsUUckpkjwsrfUBBaFR725h9IGSYw",
        "FlowIds": [
            "yDwJsUUckpkjwsr9UBBaFR17mqRADZKl",
            "yDwJsUUckpkjwsr7UBBaFRRfDjTF495Z"
        ],
        "RequestId": "s1694659168343332780"
    }
}
```

**Example 3: 集团主企业代子企业创建一个有两份子合同的合同组签署流程（B2B、B2C）**

1. 集团主企业待子企业发起，Agent.ProxyOrganizationId 需要设置为子企业的组织ID
2. 子合同1为B2C合同，Approvers中包含两个ApproverInfo元素，C端签署人ApproverType为1，企业签署人ApproverType为0。
3. 子合同2为B2B合同，Approvers中包含两个ApproverInfo元素，企业签署人ApproverType为0。

Input: 

```
tccli ess CreateFlowGroupByTemplates --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Agent.ProxyOrganizationId yDxbWUyKQDxgXVUuO5zjEB8mxCcDfAyF \
    --FlowGroupName 示例合同组-有2份子合同 \
    --FlowGroupInfos.0.TemplateId yDwXhUUckp7fs563UyNzLyWRHKWco8JV \
    --FlowGroupInfos.0.FlowName 子合同1-B2C \
    --FlowGroupInfos.0.Components.0.ComponentName 单行文本 \
    --FlowGroupInfos.0.Components.0.ComponentValue 单行文本测试 \
    --FlowGroupInfos.0.Components.0.ComponentType TEXT \
    --FlowGroupInfos.0.Components.0.FileIndex 0 \
    --FlowGroupInfos.0.Components.0.ComponentHeight 0 \
    --FlowGroupInfos.0.Components.0.ComponentWidth 0 \
    --FlowGroupInfos.0.Components.0.ComponentPage 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosX 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosY 0 \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.TemplateId yDwJ4UUckpk84g04UyPWcjIEMPGLGe2z \
    --FlowGroupInfos.1.FlowName 子合同2 \
    --FlowGroupInfos.1.FlowDescription 子合同2-B2B \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Unordered True
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwJsUUckpkjwsrfUBBaFR824h9IGSYw",
        "FlowIds": [
            "yDwJqUUckpkjwsr9UBBaFR15mqRADZKl",
            "yDwJqUUckpkjwsr7UBBaFRRfDjTF595Z"
        ],
        "RequestId": "s1695759168343332980"
    }
}
```

**Example 4: 创建一个有两份子合同的合同组签署流程（B2B、B2C），指定每个子合同第一方为动态签署方**

1. 子合同1为B2C合同，Approvers中包含两个ApproverInfo元素，C端签署人ApproverType为1，企业签署人ApproverType为0

2. 子合同1使用模板yDwXhUUckp7fs563UyNzLyWRHKWco8JV发起B端自动签署合同。需要确保在创建模板时，模板中已经指定了本企业的印章控件，否则合同发起将会失败。

3. 子合同2为B2B合同，Approvers中包含两个ApproverInfo元素，企业签署人ApproverType为0。

4.两份字合同指定一份为动态签署方（即不指定具体签署人，FillType=1），可在发起后再进行补充。

Input: 

```
tccli ess CreateFlowGroupByTemplates --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowGroupName 示例合同组-有2份子合同 \
    --FlowGroupInfos.0.TemplateId yDwXhUUckp7fs563UyNzLyWRHKWco8JV \
    --FlowGroupInfos.0.FlowName 子合同1-B2C \
    --FlowGroupInfos.0.Components.0.ComponentName 单行文本 \
    --FlowGroupInfos.0.Components.0.ComponentValue 单行文本测试 \
    --FlowGroupInfos.0.Components.0.ComponentType TEXT \
    --FlowGroupInfos.0.Components.0.FileIndex 0 \
    --FlowGroupInfos.0.Components.0.ComponentHeight 0 \
    --FlowGroupInfos.0.Components.0.ComponentWidth 0 \
    --FlowGroupInfos.0.Components.0.ComponentPage 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosX 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosY 0 \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.0.ApproverRoleName 甲方 \
    --FlowGroupInfos.0.Approvers.0.ApproverOption.FillType 1 \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Approvers.1.ApproverRoleName 乙方 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.TemplateId yDwJ5UUckpk84g04UyPWcjIEMPGLGe3z \
    --FlowGroupInfos.1.FlowName 子合同2 \
    --FlowGroupInfos.1.FlowDescription 子合同2-B2B \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.ApproverRoleName 甲方 \
    --FlowGroupInfos.1.Approvers.0.ApproverOption.FillType 1 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Approvers.1.ApproverRoleName 乙方 \
    --FlowGroupInfos.1.Unordered True
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "甲方",
                        "RecipientId": "yDCVHUUckpwbqoyiUx2jLf4wRXKt9ZGp",
                        "SignId": "yDCVHUUckpwbquhsUuyXGHSSbBKWsTXF"
                    },
                    {
                        "ApproverRoleName": "乙方",
                        "RecipientId": "yDCVHUUckpwbqoyeUx2jLf48NQhgRXND",
                        "SignId": "yDCVHUUckpwbquh8UuyXGHSyoakAk3Fo"
                    }
                ],
                "FlowId": "yDCVHUUckpwbquh1UuyXGHSwzvgoRD2j"
            },
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "甲方",
                        "RecipientId": "yDCVHUUckpwbqoyiUx2jLf4wRXKt9ZGp",
                        "SignId": "yDCVHUUckpwbquhjUuyXGHS1fHzeMsOc"
                    },
                    {
                        "ApproverRoleName": "乙方",
                        "RecipientId": "yDCVHUUckpwbqoyeUx2jLf48NQhgRXND",
                        "SignId": "yDCVHUUckpwbquhhUuyXGHSuZutTpZ47"
                    }
                ],
                "FlowId": "yDCVHUUckpwbquhqUuyXGHSvjmlRJtKP"
            }
        ],
        "FlowGroupId": "yDCVHUUckpwbquh3UuyXGHSkeqSxHjw8",
        "FlowIds": [
            "yDCVHUUckpwbquh1UuyXGHSwzvgoRD2j",
            "yDCVHUUckpwbquhqUuyXGHSvjmlRJtKP"
        ],
        "RequestId": "s1711350937322945880"
    }
}
```

**Example 5: 创建一个有两份子合同的合同组签署流程（B2B、B2C），并且通过参数FlowGroupOptions控制签署人通知方式。**

1.子合同1为B2C合同，Approvers中包含两个ApproverInfo元素，C端签署人ApproverType为1，企业签署人ApproverType为0。

2.子合同2为B2B合同，Approvers中包含两个ApproverInfo元素，企业签署人ApproverType为0。

3.此合同组下所有子合同，C端签署人使用手机号验证校验方式（FlowGroupOptions.ApproverVerifyType设置为MobileCheck）。

4.此合同组下所有子合同，发起方企业经办人不通知，需要发起方自行通知（FlowGroupOptions.SelfOrganizationApproverNotifyType设置为none）。

5.此合同组下所有子合同，他方企业经办人通过短信通知（FlowGroupOptions.OtherApproverNotifyType设置为sms）。

Input: 

```
tccli ess CreateFlowGroupByTemplates --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowGroupName 示例合同组-有2份子合同 \
    --FlowGroupOptions.ApproverVerifyType MobileCheck \
    --FlowGroupOptions.SelfOrganizationApproverNotifyType none \
    --FlowGroupOptions.OtherApproverNotifyType sms \
    --FlowGroupInfos.0.TemplateId yDwXhUUckp7fs563UyNzLyWRHKWco8JV \
    --FlowGroupInfos.0.FlowName 子合同1-B2C \
    --FlowGroupInfos.0.Components.0.ComponentName 单行文本 \
    --FlowGroupInfos.0.Components.0.ComponentValue 单行文本测试 \
    --FlowGroupInfos.0.Components.0.ComponentType TEXT \
    --FlowGroupInfos.0.Components.0.FileIndex 0 \
    --FlowGroupInfos.0.Components.0.ComponentHeight 0 \
    --FlowGroupInfos.0.Components.0.ComponentWidth 0 \
    --FlowGroupInfos.0.Components.0.ComponentPage 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosX 0 \
    --FlowGroupInfos.0.Components.0.ComponentPosY 0 \
    --FlowGroupInfos.0.FlowDescription 子合同1 \
    --FlowGroupInfos.0.FlowType 示例合同 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.0.Approvers.1.ApproverName 张三 \
    --FlowGroupInfos.0.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 18888888888 \
    --FlowGroupInfos.0.Unordered True \
    --FlowGroupInfos.1.TemplateId yDwJ4UUckpk84g04UyPWcjIEMPGLGe2z \
    --FlowGroupInfos.1.FlowName 子合同2 \
    --FlowGroupInfos.1.FlowDescription 子合同2-B2B \
    --FlowGroupInfos.1.FlowType 示例合同 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 典子谦 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 13200000000 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 李四 \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 15100000000 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 李四示例企业 \
    --FlowGroupInfos.1.Unordered True
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwJsUUckpkjwsrfUBBaFR824h9IGSYw",
        "FlowIds": [
            "yDwJsUUckpkjwsr9UBBaFR23mqRADQKl",
            "yDwJsUUckpkjwsr8UBBaFRRfDjTF295Q"
        ],
        "RequestId": "s1694659169343332980"
    }
}
```

