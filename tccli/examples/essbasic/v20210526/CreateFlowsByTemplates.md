**Example 1: 发起一份 BBC 流程**

发起一份 BBC 签署流程
其中第一方 B 为子客，即 ApproverType = ORGANIZATION，需要传递子客的 OrganizationOpenId， OrganizationName，经办人的 OpenId，Name 和 Mobile
第二方 B 为渠道外企业，即 SaaS 企业， 即 ApproverType=ORGANIZATION且NotChannelOrganization=True，需要传递企业的  OrganizationName，经办人的 Name 和 Mobile
第三方为个人，即ApproverType =  PERSON， 只需要传递 Name 和 Mobile 即可

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw \
    --FlowInfos.0.FlowName 三方签署合同 \
    --FlowInfos.0.FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowInfos.0.FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowInfos.0.FlowApprovers.0.OpenId n9527 \
    --FlowInfos.0.FlowApprovers.0.Name 典子谦 \
    --FlowInfos.0.FlowApprovers.0.Mobile 13200000000 \
    --FlowInfos.0.FlowApprovers.0.Deadline 1989688460 \
    --FlowInfos.0.FlowApprovers.0.RecipientId yDRSOUUgygqno04sUuO4zjEugoGg49nT \
    --FlowInfos.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.1.NotChannelOrganization True \
    --FlowInfos.0.FlowApprovers.1.OrganizationName 张三示例企业 \
    --FlowInfos.0.FlowApprovers.1.Name 张三 \
    --FlowInfos.0.FlowApprovers.1.Mobile 18888888888 \
    --FlowInfos.0.FlowApprovers.1.Deadline 1989688460 \
    --FlowInfos.0.FlowApprovers.1.RecipientId yDRSOUUgygqno04jUuO4zjE8SXYVwrjH \
    --FlowInfos.0.FlowApprovers.2.ApproverType PERSON \
    --FlowInfos.0.FlowApprovers.2.Name 李四 \
    --FlowInfos.0.FlowApprovers.2.Mobile 15100000000 \
    --FlowInfos.0.FlowApprovers.2.Deadline 1989688460 \
    --FlowInfos.0.FlowApprovers.2.RecipientId yDRSOUUgygqno043UuO4zjE8NnYYihhQ \
    --FlowInfos.0.Deadline 2089688460 \
    --FlowInfos.0.TemplateId yDRSOUUgygqnordgUuO4zjE8NqahJdam
```

Output: 
```
{
    "Response": {
        "CustomerData": [],
        "ErrorMessages": [
            ""
        ],
        "FlowApprovers": [
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "典子谦示例企业",
                        "RecipientId": "yDRSOUUgygqno04sUuO4zjEugoGg49nT",
                        "SignId": "yDCNsUUckpvs1o70UuxBSommqdahMmPb"
                    },
                    {
                        "ApproverRoleName": "企业签署方1",
                        "RecipientId": "yDRSOUUgygqno04jUuO4zjE8SXYVwrjH",
                        "SignId": "yDCNsUUckpvs1o7pUuxBSomCdAKFk0MP"
                    },
                    {
                        "ApproverRoleName": "个人签署方1",
                        "RecipientId": "yDRSOUUgygqno043UuO4zjE8NnYYihhQ",
                        "SignId": "yDCNsUUckpvs1o7nUuxBSomy9T24RbPy"
                    }
                ],
                "FlowId": "yDCNsUUckpvs1o75UuxBSomCyxVzORYK"
            }
        ],
        "FlowIds": [
            "yDCNsUUckpvs1o75UuxBSomCyxVzORYK"
        ],
        "PreviewUrls": [
            ""
        ],
        "RequestId": "s1706113495983439953",
        "TaskInfos": [
            {
                "TaskId": "",
                "TaskStatus": ""
            }
        ]
    }
}
```

**Example 2: 带填写控件的B2B模板发起示例**

发起一份B2B 合同（流程），双方企业均已认证，并且设置了一个发起方填写控件，控件 Name 是姓名。

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw \
    --FlowInfos.0.FlowName 测试流程一 \
    --FlowInfos.0.TemplateId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --FlowInfos.0.FlowDescription 测试流程一的描述信息 \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.0.OrganizationOpenId org_zhangsan \
    --FlowInfos.0.FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowInfos.0.FlowApprovers.0.OpenId n02468 \
    --FlowInfos.0.FlowApprovers.0.RecipientId yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpeI \
    --FlowInfos.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.1.OpenId n02468 \
    --FlowInfos.0.FlowApprovers.1.OrganizationOpenId org_zhangsan \
    --FlowInfos.0.FlowApprovers.1.OrganizationName 张三示例企业 \
    --FlowInfos.0.FlowApprovers.1.RecipientId yDxZzUyKQDKuihUuO4zjEy09jfapyHjn
```

Output: 
```
{
    "Response": {
        "CustomerData": [
            ""
        ],
        "ErrorMessages": [
            ""
        ],
        "FlowApprovers": [
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "典子谦示例企业",
                        "RecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpeI",
                        "SignId": "yDCNsUUckpvsadteUEEw4Igush87GzOR"
                    },
                    {
                        "ApproverRoleName": "张三示例企业",
                        "RecipientId": "yDxZzUyKQDKuihUuO4zjEy09jfapyHjn",
                        "SignId": "yDCNsUUckpvsadtzUEEw4IgycXgrG82a"
                    }
                ],
                "FlowId": "yDCNsUUckpvsadtiUEEw4Ig1G1ybk1QY"
            }
        ],
        "FlowIds": [
            "yDCNsUUckpvsadtiUEEw4Ig1G1ybk1QY"
        ],
        "PreviewUrls": [
            ""
        ],
        "RequestId": "s1706111849162794392",
        "TaskInfos": [
            {
                "TaskId": "",
                "TaskStatus": ""
            }
        ]
    }
}
```

**Example 3: 使用模板批量创建两个签署流程**

使用模板批量创建两个签署流程
第一个签署流程是 一个 单 C 合同，有发起方控件姓名，在发起的时候进行了填充， 即在 formfields 中填入了 components 对象
第二个签署流程是 一个 C2B 合同， 第一方 ApproverType 设置为 PERSON，第二方的 ApproverType设置为 ORGANIZATION， 有发起方控件姓名，在发起的时候进行了填充， 即在 formfields 中填入了 components 对象

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw \
    --FlowInfos.0.FlowName 测试签署流程一 \
    --FlowInfos.0.TemplateId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --FlowInfos.0.FlowDescription 测试签署流程一的描述信息 \
    --FlowInfos.0.Deadline 1989688460 \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.ApproverType PERSON \
    --FlowInfos.0.FlowApprovers.0.Name 李四 \
    --FlowInfos.0.FlowApprovers.0.Mobile 13888888888 \
    --FlowInfos.0.FlowApprovers.0.RecipientId yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpeI \
    --FlowInfos.1.FlowName 测试签署流程二 \
    --FlowInfos.1.TemplateId yDRS4UUgygqdcj56UuO4zjExBQcOiB68 \
    --FlowInfos.1.FlowDescription 测试签署流程二的描述信息 \
    --FlowInfos.1.CallbackUrl  \
    --FlowInfos.1.FormFields.0.ComponentName 姓名 \
    --FlowInfos.1.FormFields.0.ComponentValue 张三 \
    --FlowInfos.1.Deadline 1989688460 \
    --FlowInfos.1.FlowApprovers.0.Name 典子谦 \
    --FlowInfos.1.FlowApprovers.0.ApproverType PERSON \
    --FlowInfos.1.FlowApprovers.0.Mobile 13200000000 \
    --FlowInfos.1.FlowApprovers.0.RecipientId yDxZzUyKQDKuihUuO4zjEy09jfapyHjn \
    --FlowInfos.1.FlowApprovers.1.Name 张三 \
    --FlowInfos.1.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.1.FlowApprovers.1.OrganizationOpenId ess_open_organization_1 \
    --FlowInfos.1.FlowApprovers.1.OrganizationName org_zhangsan \
    --FlowInfos.1.FlowApprovers.1.Mobile 18888888888 \
    --FlowInfos.1.FlowApprovers.1.OpenId n02468 \
    --FlowInfos.1.FlowApprovers.1.RecipientId yDwJ0UUckpk2077lUxgm9jJ9eZgZChJe
```

Output: 
```
{
    "Response": {
        "CustomerData": [
            ""
        ],
        "ErrorMessages": [
            ""
        ],
        "FlowApprovers": [
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "个人签署方",
                        "RecipientId": "yDwJ2UUckpk1rwrdUrWKfEcuxn5DMpeI",
                        "SignId": "yDCNsUUckpvsadteUEEw4Igush89GzOR"
                    }
                ],
                "FlowId": "yDCNsUUckpvsadtiUEEw4Ig1G1yak1QY"
            },
            {
                "Approvers": [
                    {
                        "ApproverRoleName": "个人签署方",
                        "RecipientId": "yDxZzUyKQDKuihUuO4zjEy09jfapyHjn",
                        "SignId": "yDCNsUUckpvsadteUEEw4Igush87GzOR"
                    },
                    {
                        "ApproverRoleName": "张三示例企业",
                        "RecipientId": "yDwJ0UUckpk2077lUxgm9jJ9eZgZChJe",
                        "SignId": "yDCNsUUckpvsadtzUEEw4IgycXgrG82a"
                    }
                ],
                "FlowId": "yDCNsUUckpvsadtiUEEw4Ig1G1ybk1QY"
            }
        ],
        "FlowIds": [
            "yDCNsUUckpvsadtiUEEw4Ig1G1yak1QY",
            "yDCNsUUckpvsadtiUEEw4Ig1G1ybk1QY"
        ],
        "PreviewUrls": [
            "",
            ""
        ],
        "RequestId": "s1706111849162794392",
        "TaskInfos": [
            {
                "TaskId": "",
                "TaskStatus": ""
            },
            {
                "TaskId": "",
                "TaskStatus": ""
            }
        ]
    }
}
```

**Example 4: 创建含有动态签署人流程，签署方不指定具体的签署人**

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

