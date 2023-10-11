**Example 1: B2B 模板发起示例**

双方企业均已认证 发起示例

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId d7c13a8b***********68c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc***********3aff766cac \
    --Agent.AppId 65fb0c59***********a382cc5ed0e \
    --FlowInfos.0.FlowName 测试流程一 \
    --FlowInfos.0.TemplateId 005c***********4f7f64e8c \
    --FlowInfos.0.FlowDescription 测试流程一的描述信息 \
    --FlowInfos.0.FlowType 合同 \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.CallbackUrl  \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.0.OpenId 00498cc8***********aff766cac \
    --FlowInfos.0.FlowApprovers.0.RecipientId yDxjbUU***********zjEuCkSaxt8n \
    --FlowInfos.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.1.OpenId eezi_openid \
    --FlowInfos.0.FlowApprovers.1.OrganizationOpenId organization1_open_id \
    --FlowInfos.0.FlowApprovers.1.OrganizationName 鹅鹅子的企业 \
    --FlowInfos.0.FlowApprovers.1.RecipientId yDxjbUU***********ChJBkK7qS
```

Output: 
```
{
    "Response": {
        "CustomerData": [
            ""
        ],
        "FlowIds": [
            "yDxMqU***********vaigGvi"
        ],
        "PreviewUrls": [
            ""
        ],
        "ErrorMessages": [
            ""
        ],
        "TaskInfos": [
            {
                "TaskId": "taskid",
                "TaskStatus": "status"
            }
        ],
        "RequestId": "s16294xxxxx0001803"
    }
}
```

**Example 2: 使用模板批量创建签署流程**

使用模板批量创建签署流程

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId d7c13a8***********0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc***********3aff766cac \
    --Agent.AppId 65f***********aa382cc5ed0e \
    --FlowInfos.0.FlowName 测试签署流程一 \
    --FlowInfos.0.TemplateId 005c7f***********4f7f64e8c \
    --FlowInfos.0.FlowDescription 测试签署流程一的描述信息 \
    --FlowInfos.0.FlowType 合同 \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.CallbackUrl  \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.Name 李四 \
    --FlowInfos.0.FlowApprovers.0.Mobile 13888888888 \
    --FlowInfos.0.FlowApprovers.0.Deadline 1604910798 \
    --FlowInfos.1.FlowName 测试签署流程二 \
    --FlowInfos.1.TemplateId 005c7***********oqwnrf4e8c \
    --FlowInfos.1.FlowDescription 测试签署流程二的描述信息 \
    --FlowInfos.1.FlowType 合同 \
    --FlowInfos.1.Deadline 1604910797 \
    --FlowInfos.1.CallbackUrl  \
    --FlowInfos.1.FormFields.0.ComponentName 姓名 \
    --FlowInfos.1.FormFields.0.ComponentValue 张三 \
    --FlowInfos.1.FlowApprovers.0.Name 鹅鹅子 \
    --FlowInfos.1.FlowApprovers.0.ApproverType PERSON \
    --FlowInfos.1.FlowApprovers.0.Mobile 13200000000 \
    --FlowInfos.1.FlowApprovers.0.Deadline 1663336465 \
    --FlowInfos.1.FlowApprovers.1.Name 发起方 \
    --FlowInfos.1.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.1.FlowApprovers.1.Mobile 13700000000 \
    --FlowInfos.1.FlowApprovers.1.OpenId 12345678 \
    --FlowInfos.1.FlowApprovers.1.Deadline 1663336465
```

Output: 
```
{
    "Response": {
        "CustomerData": [
            "",
            ""
        ],
        "FlowIds": [
            "yDxM***********trvvaigGvi",
            "yDxMq***********1trvvaigGv2"
        ],
        "PreviewUrls": [
            "",
            ""
        ],
        "ErrorMessages": [
            "",
            ""
        ],
        "TaskInfos": [
            {
                "TaskId": "taskid",
                "TaskStatus": "status"
            }
        ],
        "RequestId": "s162944xxxxx3"
    }
}
```

**Example 3: 创建含有动态签署人流程，签署方不指定具体的签署人**

创建一个B2C流程，两方签署方不指定具体的签署人
注： 
`1.签署人相关信息为空，如：姓名、手机号码等` 
`2.FillType需传值为1，表示为动态签署人（不确定具体的签署人），需后续进行补充。` 
`3.需保留对应的角色编号，即RecipientId，后续补充具体的签署人时需指定对应的RecipientId`

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId d7c13a8b***********68c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc***********3aff766cac \
    --Agent.AppId 65fb0c59***********a382cc5ed0e \
    --FlowInfos.0.FlowName 测试流程一 \
    --FlowInfos.0.TemplateId 005c***********4f7f64e8c \
    --FlowInfos.0.FlowDescription 测试流程一的描述信息 \
    --FlowInfos.0.FlowType 合同 \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.CallbackUrl  \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.0.ApproverRoleName 企业签署方 \
    --FlowInfos.0.FlowApprovers.0.RecipientId yDxjbUU***********zjEuCkSaxt8n \
    --FlowInfos.0.FlowApprovers.0.ApproverOption.FillType 1 \
    --FlowInfos.0.FlowApprovers.1.ApproverType PERSON \
    --FlowInfos.0.FlowApprovers.1.ApproverRoleName 个人签署方 \
    --FlowInfos.0.FlowApprovers.1.RecipientId yDxjbUU***********ChJBkK7qS \
    --FlowInfos.0.FlowApprovers.1.ApproverOption.FillType 1
```

Output: 
```
{
    "Response": {
        "CustomerData": [
            ""
        ],
        "FlowIds": [
            "yDxMqU***********vaigGvi"
        ],
        "PreviewUrls": [
            ""
        ],
        "ErrorMessages": [
            ""
        ],
        "TaskInfos": [
            {
                "TaskId": "taskid",
                "TaskStatus": "status"
            }
        ],
        "FlowApprovers": [
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "企业签署方",
                        "RecipientId": "yDxjbUU***********zjEuCkSaxt8n",
                        "SignId": "yDw7hUUckpkmtvenURxlqRxRcrWD0zVk"
                    },
                    {
                        "ApproverRoleName": "个人签署方",
                        "RecipientId": "yDxjbUU***********ChJBkK7qS",
                        "SignId": "yDw7hUUckpkmtvegURxlqRxSV5qDMex1"
                    }
                ],
                "FlowId": "yDxMqU***********vaigGvi"
            }
        ],
        "RequestId": "s16294xxxxx0001803"
    }
}
```

