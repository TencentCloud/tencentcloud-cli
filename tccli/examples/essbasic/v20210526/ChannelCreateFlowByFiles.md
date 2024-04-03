**Example 1: 使用文件创建B2B2C的合同**

1. 包含<b>个人/自然人</b>签署 <b>张三</b>
2. 包含第三方子企业<b>李四的示例企业</b>员工<b>李四</b>
3. 包含平台企业<b>王五示例企业</b>的员工<b>王五</b> (NotChannelOrganization设置为true)
4. 王五的签署区是通过关键字<b>甲方签章位置</b>生成印章区域

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowName 购买50吨西红柿的合同(15:53:35) \
    --FlowApprovers.0.Name 张三 \
    --FlowApprovers.0.Mobile 18888888888 \
    --FlowApprovers.0.ApproverType PERSON \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 112 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 40 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 146.15625 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 472.78125 \
    --FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FlowApprovers.1.Name 李四 \
    --FlowApprovers.1.Mobile 17333333333 \
    --FlowApprovers.1.OrganizationName 李四的示例企业 \
    --FlowApprovers.1.OpenId lisi \
    --FlowApprovers.1.OrganizationOpenId org_lisi \
    --FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 112 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 40 \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 146.15625 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 472.78125 \
    --FlowApprovers.1.SignComponents.0.ComponentValue  \
    --FlowApprovers.2.Name 王五 \
    --FlowApprovers.2.Mobile 13333333333 \
    --FlowApprovers.2.OrganizationName 王五示例企业 \
    --FlowApprovers.2.NotChannelOrganization True \
    --FlowApprovers.2.ApproverType ORGANIZATION \
    --FlowApprovers.2.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.2.SignComponents.0.FileIndex 0 \
    --FlowApprovers.2.SignComponents.0.ComponentWidth 112 \
    --FlowApprovers.2.SignComponents.0.ComponentHeight 40 \
    --FlowApprovers.2.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.2.SignComponents.0.ComponentPosX 146.15625 \
    --FlowApprovers.2.SignComponents.0.ComponentPosY 472.78125 \
    --FlowApprovers.2.SignComponents.0.ComponentValue  \
    --FlowApprovers.2.SignComponents.1.ComponentId 甲方签章位置 \
    --FlowApprovers.2.SignComponents.1.ComponentType SIGN_SEAL \
    --FlowApprovers.2.SignComponents.1.GenerateMode KEYWORD \
    --FlowApprovers.2.SignComponents.1.ComponentWidth 112 \
    --FlowApprovers.2.SignComponents.1.ComponentHeight 40 \
    --FileIds yDSLoUUckpob08ffUxVoXTnu6fPhgjmx \
    --Unordered True
```

Output: 
```
{
    "Response": {
        "FlowId": "yDSLoUUckpob829aUxvfkKfCKWvrOGyb",
        "Approvers": [
            {
                "SignId": "yDSLoUUckpob829wUxvfkKfCOwpAOD9N",
                "RecipientId": "yDSLoUUckpob829yUxvfkKfssEItYFKp",
                "ApproverRoleName": ""
            },
            {
                "SignId": "yDSLoUUckpob829tUxvfkKfuX06FFWEw",
                "RecipientId": "yDSLoUUckpob829vUxvfkKf83OAYth3A",
                "ApproverRoleName": ""
            },
            {
                "SignId": "yDSLoUUckpob829kUxvfkKfuiREpXebq",
                "RecipientId": "yDSLoUUckpob829oUxvfkKfwRMwMrwrM",
                "ApproverRoleName": ""
            }
        ],
        "RequestId": "6545213e-4554-4839-a69d-6ef75344c749"
    }
}
```

**Example 2: 使用文件创建单自然人签署的合同**

发起只有<b>个人/自然人</b>签署 <b>张三</b>来签署的合同

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId 110101200610116558 \
    --Agent.ProxyAppId  \
    --FlowName 西瓜采购协议(16:18:47) \
    --FlowApprovers.0.Name 张三 \
    --FlowApprovers.0.Mobile 18888888888 \
    --FlowApprovers.0.ApproverType PERSON \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 112 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 40 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 146.15625 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 472.78125 \
    --FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FileIds yDSLoUUckpob089cUxVoXTn9T1cRb8W7 \
    --Unordered True
```

Output: 
```
{
    "Response": {
        "FlowId": "yDSLoUUckpobjhymUyKMWsdBQKTeh0lS",
        "Approvers": [
            {
                "SignId": "yDSLoUUckpobjhy9UyKMWsdSJ1PF1kag",
                "RecipientId": "yDSLoUUckpobjhyfUyKMWsdxqy3zpae2",
                "ApproverRoleName": ""
            }
        ],
        "RequestId": "c98e62a4-8577-4d78-87d6-16519fcd17e7"
    }
}
```

**Example 3: 创建一个B2C合同，签署人和发起方都有填写控件**

1.通过PDF文件发起合同
2.指定B端签署方为企业【典子谦示例企业】，经办人OpenId 是 n9527
3.指定C端签署方为个人【张三】
4.发起方填写控件为通过外层 参数 Components 传递，需要在发起时通过 ComponentValue 指定值
5.签署方填写控件通过Approvers.Components传递，在发起时不能通过 ComponentValue 指定值，需要签署人在合同成功发起后自己填写
6.更多签署方填写控件示例 可参考文档 [指定签署方填写控件](https://qian.tencent.com/developers/partner/createFlowByFiles#%E4%B8%BA%E7%AD%BE%E7%BD%B2%E6%96%B9%E6%8C%87%E5%AE%9A%E5%A1%AB%E5%86%99%E6%8E%A7%E4%BB%B6)

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.AppId yDCVsUUckpw2nwxkUxRytJLxpswCHW2m \
    --FlowName B2C-签署方有填写控件 \
    --Components.0.ComponentHeight 20 \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 205 \
    --Components.0.ComponentPosY 90 \
    --Components.0.ComponentValue （落霞与孤鹜齐飞，秋水共长天一色）这是发起方填写的文本 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentWidth 339 \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 119 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 7 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 143.59375 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 169.0625 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.0.Components.0.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-CREDIT-CODE"} \
    --FlowApprovers.0.Components.0.ComponentHeight 20 \
    --FlowApprovers.0.Components.0.ComponentPage 1 \
    --FlowApprovers.0.Components.0.ComponentPosX 205 \
    --FlowApprovers.0.Components.0.ComponentPosY 114 \
    --FlowApprovers.0.Components.0.ComponentRequired False \
    --FlowApprovers.0.Components.0.ComponentType TEXT \
    --FlowApprovers.0.Components.0.ComponentWidth 339 \
    --FlowApprovers.0.Components.1.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-CREDIT-CODE"} \
    --FlowApprovers.0.Components.1.ComponentHeight 20 \
    --FlowApprovers.0.Components.1.ComponentPage 1 \
    --FlowApprovers.0.Components.1.ComponentPosX 234 \
    --FlowApprovers.0.Components.1.ComponentPosY 142 \
    --FlowApprovers.0.Components.1.ComponentRequired False \
    --FlowApprovers.0.Components.1.ComponentType TEXT \
    --FlowApprovers.0.Components.1.ComponentWidth 302 \
    --FlowApprovers.0.Components.2.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-LEGAL-NAME"} \
    --FlowApprovers.0.Components.2.ComponentHeight 20 \
    --FlowApprovers.0.Components.2.ComponentPage 1 \
    --FlowApprovers.0.Components.2.ComponentPosX 191.09 \
    --FlowApprovers.0.Components.2.ComponentPosY 172 \
    --FlowApprovers.0.Components.2.ComponentRequired False \
    --FlowApprovers.0.Components.2.ComponentType TEXT \
    --FlowApprovers.0.Components.2.ComponentWidth 335 \
    --FlowApprovers.0.Components.3.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --FlowApprovers.0.Components.3.ComponentHeight 21 \
    --FlowApprovers.0.Components.3.ComponentPage 1 \
    --FlowApprovers.0.Components.3.ComponentPosX 155 \
    --FlowApprovers.0.Components.3.ComponentPosY 205 \
    --FlowApprovers.0.Components.3.ComponentRequired False \
    --FlowApprovers.0.Components.3.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.0.Components.3.ComponentWidth 366 \
    --FlowApprovers.0.Components.4.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-NAME"} \
    --FlowApprovers.0.Components.4.ComponentHeight 20 \
    --FlowApprovers.0.Components.4.ComponentPage 1 \
    --FlowApprovers.0.Components.4.ComponentPosX 107 \
    --FlowApprovers.0.Components.4.ComponentPosY 236 \
    --FlowApprovers.0.Components.4.ComponentRequired False \
    --FlowApprovers.0.Components.4.ComponentType TEXT \
    --FlowApprovers.0.Components.4.ComponentWidth 339 \
    --FlowApprovers.0.Components.5.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-MOBILE"} \
    --FlowApprovers.0.Components.5.ComponentHeight 20 \
    --FlowApprovers.0.Components.5.ComponentPage 1 \
    --FlowApprovers.0.Components.5.ComponentPosX 121 \
    --FlowApprovers.0.Components.5.ComponentPosY 265 \
    --FlowApprovers.0.Components.5.ComponentRequired False \
    --FlowApprovers.0.Components.5.ComponentType TEXT \
    --FlowApprovers.0.Components.5.ComponentWidth 327 \
    --FlowApprovers.0.Components.6.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --FlowApprovers.0.Components.6.ComponentHeight 20 \
    --FlowApprovers.0.Components.6.ComponentPage 1 \
    --FlowApprovers.0.Components.6.ComponentPosX 35.09 \
    --FlowApprovers.0.Components.6.ComponentPosY 293 \
    --FlowApprovers.0.Components.6.ComponentRequired False \
    --FlowApprovers.0.Components.6.ComponentType DISTRICT \
    --FlowApprovers.0.Components.6.ComponentWidth 306 \
    --FlowApprovers.0.Components.7.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --FlowApprovers.0.Components.7.ComponentHeight 44 \
    --FlowApprovers.0.Components.7.ComponentPage 1 \
    --FlowApprovers.0.Components.7.ComponentPosX 44 \
    --FlowApprovers.0.Components.7.ComponentPosY 652 \
    --FlowApprovers.0.Components.7.ComponentRequired False \
    --FlowApprovers.0.Components.7.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.0.Components.7.ComponentWidth 505 \
    --FlowApprovers.0.Components.8.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"DIGIT"} \
    --FlowApprovers.0.Components.8.ComponentHeight 20 \
    --FlowApprovers.0.Components.8.ComponentPage 1 \
    --FlowApprovers.0.Components.8.ComponentPosX 191 \
    --FlowApprovers.0.Components.8.ComponentPosY 716 \
    --FlowApprovers.0.Components.8.ComponentRequired False \
    --FlowApprovers.0.Components.8.ComponentType TEXT \
    --FlowApprovers.0.Components.8.ComponentWidth 35 \
    --FlowApprovers.0.Components.9.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","ManualFill":true} \
    --FlowApprovers.0.Components.9.ComponentHeight 20 \
    --FlowApprovers.0.Components.9.ComponentPage 2 \
    --FlowApprovers.0.Components.9.ComponentPosX 145 \
    --FlowApprovers.0.Components.9.ComponentPosY 68 \
    --FlowApprovers.0.Components.9.ComponentRequired False \
    --FlowApprovers.0.Components.9.ComponentType DATE \
    --FlowApprovers.0.Components.9.ComponentWidth 116 \
    --FlowApprovers.0.Components.10.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"DIGIT"} \
    --FlowApprovers.0.Components.10.ComponentHeight 20 \
    --FlowApprovers.0.Components.10.ComponentPage 2 \
    --FlowApprovers.0.Components.10.ComponentPosX 194.09 \
    --FlowApprovers.0.Components.10.ComponentPosY 92.09 \
    --FlowApprovers.0.Components.10.ComponentRequired False \
    --FlowApprovers.0.Components.10.ComponentType TEXT \
    --FlowApprovers.0.Components.10.ComponentWidth 326 \
    --FlowApprovers.0.Components.11.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","ManualFill":true} \
    --FlowApprovers.0.Components.11.ComponentHeight 20 \
    --FlowApprovers.0.Components.11.ComponentPage 2 \
    --FlowApprovers.0.Components.11.ComponentPosX 130.09375 \
    --FlowApprovers.0.Components.11.ComponentPosY 555.09375 \
    --FlowApprovers.0.Components.11.ComponentRequired False \
    --FlowApprovers.0.Components.11.ComponentType DATE \
    --FlowApprovers.0.Components.11.ComponentWidth 116 \
    --FlowApprovers.0.Components.12.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --FlowApprovers.0.Components.12.ComponentHeight 27 \
    --FlowApprovers.0.Components.12.ComponentPage 2 \
    --FlowApprovers.0.Components.12.ComponentPosX 134.09 \
    --FlowApprovers.0.Components.12.ComponentPosY 628.09 \
    --FlowApprovers.0.Components.12.ComponentRequired False \
    --FlowApprovers.0.Components.12.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.0.Components.12.ComponentWidth 398 \
    --FlowApprovers.0.Components.13.ComponentExtra {"Values":["选项1","当面交货","送货上门","寄放到公证处"],"FontSize":12,"FontAlign":"Left","Font":"黑体","MultiSelect":false} \
    --FlowApprovers.0.Components.13.ComponentHeight 20 \
    --FlowApprovers.0.Components.13.ComponentPage 2 \
    --FlowApprovers.0.Components.13.ComponentPosX 141.09 \
    --FlowApprovers.0.Components.13.ComponentPosY 656.09 \
    --FlowApprovers.0.Components.13.ComponentRequired False \
    --FlowApprovers.0.Components.13.ComponentType SELECTOR \
    --FlowApprovers.0.Components.13.ComponentWidth 216 \
    --FlowApprovers.0.Components.14.ComponentExtra {} \
    --FlowApprovers.0.Components.14.ComponentHeight 16 \
    --FlowApprovers.0.Components.14.ComponentPage 7 \
    --FlowApprovers.0.Components.14.ComponentPosX 83.09375 \
    --FlowApprovers.0.Components.14.ComponentPosY 96.5625 \
    --FlowApprovers.0.Components.14.ComponentType CHECK_BOX \
    --FlowApprovers.0.Components.14.ComponentWidth 16 \
    --FlowApprovers.1.Name 张三 \
    --FlowApprovers.1.Mobile 18700000000 \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 43 \
    --FlowApprovers.1.SignComponents.0.ComponentPage 7 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 433.59375 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 196.0625 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.1.Components.0.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-NAME"} \
    --FlowApprovers.1.Components.0.ComponentHeight 20 \
    --FlowApprovers.1.Components.0.ComponentPage 1 \
    --FlowApprovers.1.Components.0.ComponentPosX 199 \
    --FlowApprovers.1.Components.0.ComponentPosY 323 \
    --FlowApprovers.1.Components.0.ComponentRequired False \
    --FlowApprovers.1.Components.0.ComponentType TEXT \
    --FlowApprovers.1.Components.0.ComponentWidth 309 \
    --FlowApprovers.1.Components.1.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-IDCARD"} \
    --FlowApprovers.1.Components.1.ComponentHeight 20 \
    --FlowApprovers.1.Components.1.ComponentPage 1 \
    --FlowApprovers.1.Components.1.ComponentPosX 124.09 \
    --FlowApprovers.1.Components.1.ComponentPosY 352 \
    --FlowApprovers.1.Components.1.ComponentRequired False \
    --FlowApprovers.1.Components.1.ComponentType TEXT \
    --FlowApprovers.1.Components.1.ComponentWidth 327 \
    --FlowApprovers.1.Components.2.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --FlowApprovers.1.Components.2.ComponentHeight 24 \
    --FlowApprovers.1.Components.2.ComponentPage 1 \
    --FlowApprovers.1.Components.2.ComponentPosX 155 \
    --FlowApprovers.1.Components.2.ComponentPosY 386 \
    --FlowApprovers.1.Components.2.ComponentRequired False \
    --FlowApprovers.1.Components.2.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.1.Components.2.ComponentWidth 390 \
    --FlowApprovers.1.Components.3.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --FlowApprovers.1.Components.3.ComponentHeight 20 \
    --FlowApprovers.1.Components.3.ComponentPage 1 \
    --FlowApprovers.1.Components.3.ComponentPosX 114.09 \
    --FlowApprovers.1.Components.3.ComponentPosY 416 \
    --FlowApprovers.1.Components.3.ComponentRequired False \
    --FlowApprovers.1.Components.3.ComponentType TEXT \
    --FlowApprovers.1.Components.3.ComponentWidth 299 \
    --FlowApprovers.1.Components.4.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-MOBILE"} \
    --FlowApprovers.1.Components.4.ComponentHeight 20 \
    --FlowApprovers.1.Components.4.ComponentPage 1 \
    --FlowApprovers.1.Components.4.ComponentPosX 115.09 \
    --FlowApprovers.1.Components.4.ComponentPosY 445 \
    --FlowApprovers.1.Components.4.ComponentRequired False \
    --FlowApprovers.1.Components.4.ComponentType TEXT \
    --FlowApprovers.1.Components.4.ComponentWidth 367 \
    --FlowApprovers.1.Components.5.ComponentExtra {"SubType":"EDUCATION"} \
    --FlowApprovers.1.Components.5.ComponentHeight 20 \
    --FlowApprovers.1.Components.5.ComponentId ComponentId_30 \
    --FlowApprovers.1.Components.5.ComponentName 学历 \
    --FlowApprovers.1.Components.5.ComponentPage 1 \
    --FlowApprovers.1.Components.5.ComponentPosX 8.09375 \
    --FlowApprovers.1.Components.5.ComponentPosY 473 \
    --FlowApprovers.1.Components.5.ComponentRequired False \
    --FlowApprovers.1.Components.5.ComponentType SELECTOR \
    --FlowApprovers.1.Components.5.ComponentWidth 84 \
    --FlowApprovers.1.Components.6.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"EMAIL"} \
    --FlowApprovers.1.Components.6.ComponentHeight 20 \
    --FlowApprovers.1.Components.6.ComponentId ComponentId_28 \
    --FlowApprovers.1.Components.6.ComponentName 邮箱 \
    --FlowApprovers.1.Components.6.ComponentPage 1 \
    --FlowApprovers.1.Components.6.ComponentPosX 117.09375 \
    --FlowApprovers.1.Components.6.ComponentPosY 474 \
    --FlowApprovers.1.Components.6.ComponentRequired False \
    --FlowApprovers.1.Components.6.ComponentType TEXT \
    --FlowApprovers.1.Components.6.ComponentWidth 292 \
    --FlowApprovers.1.Components.7.ComponentExtra {"SubType":"GENDER"} \
    --FlowApprovers.1.Components.7.ComponentHeight 20 \
    --FlowApprovers.1.Components.7.ComponentId ComponentId_29 \
    --FlowApprovers.1.Components.7.ComponentName 性别 \
    --FlowApprovers.1.Components.7.ComponentPage 1 \
    --FlowApprovers.1.Components.7.ComponentPosX 424.09375 \
    --FlowApprovers.1.Components.7.ComponentPosY 472 \
    --FlowApprovers.1.Components.7.ComponentRequired False \
    --FlowApprovers.1.Components.7.ComponentType SELECTOR \
    --FlowApprovers.1.Components.7.ComponentWidth 84 \
    --FileIds yDCWqUUckpvebypnU4f5ELvs3AdsTJp7
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCVsUUckpwri4vqU9JHnkyzivgo9ZYK",
                "SignId": "yDCVsUUckpwri2vjU0JHnkcdalTQjZVo"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCVsUUckpwri6v8U9JHnkE9wfDGvwZL",
                "SignId": "yDCVsUUckpwri3vhU9JHnkSxBnzV59Vo"
            }
        ],
        "FlowId": "yDCVsUUckpwri2vsU9JHnkuZc5pjfOMs",
        "RequestId": "s1709794795446614457"
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
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId zhangsan \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.AppId yDwFoUUckps**********yhWGhIR2RkhOjw2 \
    --Unordered True \
    --FlowName 发起动态签署人合同示例 \
    --FlowApprovers.0.Name  \
    --FlowApprovers.0.Mobile  \
    --FlowApprovers.0.ApproverType PERSON \
    --FlowApprovers.0.ApproverRoleName 个人签署方 \
    --FlowApprovers.0.ApproverOption.FillType 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 260 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowApprovers.1.ApproverRoleName 企业签署方 \
    --FlowApprovers.1.ApproverOption.FillType 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 260 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FileIds yDwFhUUckpsxas68UuZf2EREDkOykmDp
```

Output: 
```
{
    "Response": {
        "FlowId": "2fb48c3945****65aaedf6",
        "Approvers": [
            {
                "SignId": "yDw7hUUckpkm57vuUxeFIKavjSsJtcaN",
                "RecipientId": "yDw7hUUckpkm57v4UxeFIKaS5kF2iWh8",
                "ApproverRoleName": "个人签署方"
            },
            {
                "SignId": "yDw7hUUckpkm57v7UxeFIKa8kitjb9XB",
                "RecipientId": "yDw7hUUckpkm57vxUxeFIKaCJX9krcZN",
                "ApproverRoleName": "企业签署方"
            }
        ],
        "RequestId": "s1234345677xxxx"
    }
}
```

