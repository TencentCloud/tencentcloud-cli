**Example 1: 创建电子文档-缺少填写控件**

1.通过模板创建电子文档
2.未对模板内的必填控件【单行文本2】控件进行赋值

Input: 

```
tccli ess CreateDocument --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FileNames 合同文件.pdf \
    --FlowId yDwFdUUckpsvet4jUEn0aFRxtu5TdalM \
    --TemplateId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --ClientToken  \
    --NeedPreview False \
    --FormFields.0.ComponentValue 123456 \
    --FormFields.0.ComponentId 单行文本
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "控件[单行文本1]值未提交"
        },
        "RequestId": "28a7347b-xxxx-xxxx-xxxx-162c4bc230d6"
    }
}
```

**Example 2: 创建电子文档并填充内容控件**

1.设置流程合同ID为yDwFmUUckpst10i3UubBSat8PWOt2iQF
2.设置文档模板ID为yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR
3.设置模板内的图片填写控件值

Input: 

```
tccli ess CreateDocument --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FileNames 合同文件.pdf \
    --FlowId yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --TemplateId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --ClientToken  \
    --NeedPreview False \
    --FormFields.0.ComponentValue 张三的单行文本1 \
    --FormFields.0.ComponentId 单行文本填写1 \
    --FormFields.1.ComponentValue 张三的单行文本1 \
    --FormFields.1.ComponentId 单行文本填写2 \
    --FormFields.2.ComponentValue 张三的填写内容 \
    --FormFields.2.ComponentId 多行填写1 \
    --FormFields.3.ComponentValue true \
    --FormFields.3.ComponentId checkBox控件
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "****有限公司",
                "RecipientId": "yDRvoUUgygqoh024UuO4zjE8OBoGfRNr",
                "SignId": "yDw7hUUckpkmkwraUunP4DaSHZaRRhKP"
            },
            {
                "ApproverRoleName": "个人签署方1",
                "RecipientId": "yDRvoUUgygqoh02bUuO4zjE8VMs79RJy",
                "SignId": "yDw7hUUckpkmkwryUunP4Dau01y5xJRN"
            }
        ],
        "RequestId": "18b53278-xxxx-xxxx-xxxx-06aa59796573",
        "DocumentId": "yDxZ1UyKQDSIMfUuO4zjEw2TyqzKEs16",
        "PreviewFileUrl": ""
    }
}
```

**Example 3: 创建电子文档并填充图片控件**

1.设置流程合同ID为yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
2.设置文档模板ID为yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc
3.设置模板内的图片填写控件值为yDxZ1UyKQDSIMXUuO4zjERbwQIfGw4TK
注：
`若发起合同时不确定具体的签署人，即发起了含有动态签署人的合同，需保留对应的签署角色编号（即RecipientId），后续进行补充时需指定对应的RecipientId`


Input: 

```
tccli ess CreateDocument --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FileNames 合同文件.pdf \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --TemplateId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --ClientToken  \
    --NeedPreview False \
    --FormFields.0.ComponentValue yDxZ1UyKQDSIMXUuO4zjERbwQIfGw4TK \
    --FormFields.0.ComponentId component_image
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "****有限公司",
                "RecipientId": "yDRvoUUgygqoh024UuO4zjE8OBoGfRNr",
                "SignId": "yDw7hUUckpkmkwraUunP4DaSHZaRRhKP"
            },
            {
                "ApproverRoleName": "个人签署方1",
                "RecipientId": "yDRvoUUgygqoh02bUuO4zjE8VMs79RJy",
                "SignId": "yDw7hUUckpkmkwryUunP4Dau01y5xJRN"
            }
        ],
        "RequestId": "956d7f8d-xxxx-xxxx-xxxx-4e48d923ecf0",
        "DocumentId": "yDxZ1UyKQDSIMaUuO5zjEypPWudeHbnG",
        "PreviewFileUrl": ""
    }
}
```

