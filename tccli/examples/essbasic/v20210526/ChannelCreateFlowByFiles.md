**Example 1: 使用文件创建B2B2C的合同 - 同时使用关键字和绝对定位**

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

**Example 5: 处方单场景**

1.处方单场景的"典子谦"医生需要自动签(典子谦参与人的ApproverType设置成PERSON_AUTO_SIGN, 并且AutoSignScene设置成E_PRESCRIPTION_AUTO_SIGN表明是处方单场景)
2.处方单的患者张三需要手工签署(张三参与人的ApproverType设置成PERSON)
3.双方签署方的签署控件都是通过关键字生成(典子谦签署区GenerateMode设置成KEYWORD并且ComponentId设置成关键字"处方医生", 张三签署区GenerateMode设置成KEYWORD并且ComponentId设置成关键字"患者签名" )
4.不给合同签署方发送短信 (NotifyType设置成NONE)

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --FlowName 文件发起-处方单 \
    --FlowApprovers.0.ApproverType PERSON_AUTO_SIGN \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.NotifyType NONE \
    --FlowApprovers.0.SignComponents.0.GenerateMode KEYWORD \
    --FlowApprovers.0.SignComponents.0.ComponentId 处方医生 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowApprovers.0.SignComponents.0.OffsetX 100.5 \
    --FlowApprovers.0.SignComponents.0.OffsetY 200.5 \
    --FlowApprovers.0.SignComponents.1.GenerateMode KEYWORD \
    --FlowApprovers.0.SignComponents.1.ComponentId DATE \
    --FlowApprovers.0.SignComponents.1.FileIndex 0 \
    --FlowApprovers.0.SignComponents.1.ComponentType SIGN_DATE \
    --FlowApprovers.0.SignComponents.1.ComponentWidth 100 \
    --FlowApprovers.0.SignComponents.1.ComponentHeight 100 \
    --FlowApprovers.0.SignComponents.1.OffsetX 100.5 \
    --FlowApprovers.0.SignComponents.1.OffsetY 200.5 \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.Name 张三 \
    --FlowApprovers.1.Mobile 18888888888 \
    --FlowApprovers.1.NotifyType NONE \
    --FlowApprovers.1.SignComponents.0.GenerateMode KEYWORD \
    --FlowApprovers.1.SignComponents.0.ComponentId 患者签名 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FlowApprovers.1.SignComponents.0.OffsetX 100.5 \
    --FlowApprovers.1.SignComponents.0.OffsetY 200.5 \
    --FlowApprovers.1.SignComponents.1.GenerateMode KEYWORD \
    --FlowApprovers.1.SignComponents.1.ComponentId DATE1 \
    --FlowApprovers.1.SignComponents.1.FileIndex 0 \
    --FlowApprovers.1.SignComponents.1.ComponentType SIGN_DATE \
    --FlowApprovers.1.SignComponents.1.ComponentWidth 100 \
    --FlowApprovers.1.SignComponents.1.ComponentHeight 100 \
    --FlowApprovers.1.SignComponents.1.OffsetX 100.5 \
    --FlowApprovers.1.SignComponents.1.OffsetY 200.5 \
    --AutoSignScene E_PRESCRIPTION_AUTO_SIGN \
    --FileIds yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Unordered True
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiixbUyngyQvxNVFfGhPt",
                "SignId": "yDCm3UUckpuhiixaUyngyQvCEn8PpCcq"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiixyUyngyQvEiHySXVJ0",
                "SignId": "yDCm3UUckpuhiixwUyngyQvCtQdTNFcF"
            }
        ],
        "FlowId": "yDCm3UUckpuhiixuUyngyQvBQysQq7t7",
        "RequestId": "s1726221157105242252"
    }
}
```

**Example 6: 创建一份签署方拖拽签署区域的合同**

1.签署方包括本方子客企业(需要传递 OrganzationOpenId，和 OpenId)、他方SaaS企业(需要传递 NotChannelOrganization = true)和个人（Approvers中有三个ApproverInfo元素）。
2.所有签署方企业都不包允许有签署控件。
3.设置当前流程为可拖拽（SignBeanTag）。
4.本合同为无序签署（Unordered传递为true）。

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Unordered True \
    --FlowName 签署时拖拽签署控件合同 \
    --SignBeanTag 1 \
    --FlowType 示例合同 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.NotifyType NONE \
    --FlowApprovers.0.PreReadTime 10 \
    --FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowApprovers.1.NotChannelOrganization True \
    --FlowApprovers.1.OrganizationName 张三示例企业 \
    --FlowApprovers.1.Name 张三 \
    --FlowApprovers.1.Mobile 18888888888 \
    --FlowApprovers.1.NotifyType NONE \
    --FlowApprovers.1.PreReadTime 10 \
    --FlowApprovers.2.ApproverType PERSON \
    --FlowApprovers.2.NotifyType NONE \
    --FlowApprovers.2.Name 李四 \
    --FlowApprovers.2.Mobile 15100000000 \
    --FlowApprovers.2.PreReadTime 10 \
    --FileIds yDR4yUUgyg1qqlj7UuO4zjES3G9Shoxk
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiivxUyngyQvCtRL9F1iX",
                "SignId": "yDCm3UUckpuhiiv7UyngyQvweoRnofAx"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiiv4UyngyQvw4w7nChfk",
                "SignId": "yDCm3UUckpuhiivuUyngyQvCexPDjr49"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiivbUyngyQvxPc40bmBS",
                "SignId": "yDCm3UUckpuhiivaUyngyQvTjdVbIqsr"
            }
        ],
        "FlowId": "yDCm3UUckpuhiiv9UyngyQvE2eRmVW3M",
        "RequestId": "s1726285140721667651"
    }
}
```

**Example 7: 通过文件发起B2C合同-控件使用绝对定位方式**

1.通过PDF文件发起合同 
2.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】 
3.通过绝对对位方式指定【典子谦示例企业】的签署控件为印章控件，控件位置为该文件的第1页，横坐标160，纵坐标260的位置，控件高宽为119x119（公章大小） 
4.指定C端签署方为个人【李四】，联系电话为【15100000000】 
5.通过绝对对位方式指定【李四】的签署控件为手写签名控件，控件位置为该文件的第1页，横坐标60，纵坐标260的位置，控件高宽为119x43（推荐的手写签名大小） 
6.通过绝对定位方式在合同文件的第1页，横坐标360，纵坐标360的位置放置一个单行文本控件，并写入内容【我是一个单行文本】
 7.完成合同发起

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --FlowName 通过文件发起合同 \
    --FlowDescription 通过文件发起合同 \
    --Unordered False \
    --FlowType 示例合同 \
    --Deadline 1830268800 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 160 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 119 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.NotifyType NONE \
    --FlowApprovers.1.Name 李四 \
    --FlowApprovers.1.Mobile 15100000000 \
    --FlowApprovers.1.PreReadTime 10 \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 60 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 43 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
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
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiiwrUyngyQvEAAG8aSuj",
                "SignId": "yDCm3UUckpuhiiwlUyngyQvEVt11WQd6"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiiw5UyngyQvvbypsA2N5",
                "SignId": "yDCm3UUckpuhiiw0UyngyQvxIu5Rvq2L"
            }
        ],
        "FlowId": "yDCm3UUckpuhiiw2UyngyQv8OPSX8qYD",
        "RequestId": "s1726284341125380532"
    }
}
```

**Example 8: 通过文件发起B2C合同-控件使用关键字定位方式**

1.通过PDF文件发起合同 
2.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】 
3.通过绝对对位方式指定【典子谦示例企业】的签署控件为印章控件，控件类型为【KEYWORD】关键字类型，并设置关键字为【签名】，关键字查找顺序为【Positive-正序】关键字位置模式为【Middle-居中】，控件高宽为119x119（公章大小） 
4.指定C端签署方为个人【李四】，联系电话为【15100000000】 
5.通过绝对对位方式指定【李四】的签署控件为手写签名控件，控件位置为该文件的第1页，横坐标60，纵坐标260的位置，控件高宽为119x43（推荐的手写签名大小） 
6.通过绝对定位方式在合同文件的第1页，横坐标360，纵坐标360的位置放置一个单行文本控件，并写入内容【我是一个单行文本】 
7.完成合同发起

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --FlowName 通过文件发起合同-关键字定位 \
    --FlowDescription 通过文件发起合同 \
    --Unordered False \
    --FlowType 示例合同 \
    --Deadline 1830268800 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 0 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 0 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 119 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.0.SignComponents.0.GenerateMode KEYWORD \
    --FlowApprovers.0.SignComponents.0.ComponentId 签名 \
    --FlowApprovers.0.SignComponents.0.KeywordOrder Positive \
    --FlowApprovers.0.SignComponents.0.RelativeLocation Middle \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.NotifyType NONE \
    --FlowApprovers.1.Name 李四 \
    --FlowApprovers.1.Mobile 15100000000 \
    --FlowApprovers.1.PreReadTime 10 \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 60 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 43 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
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
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiivjUyngyQvwaZ4Hg4MJ",
                "SignId": "yDCm3UUckpuhiiv8UyngyQvy5NE74xeK"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiivhUyngyQvuSNWvTWW3",
                "SignId": "yDCm3UUckpuhiiv2UyngyQvwKnI8ePPG"
            }
        ],
        "FlowId": "yDCm3UUckpuhiivqUyngyQvB0ZL8Vhvu",
        "RequestId": "s1726285565082734481"
    }
}
```

**Example 9: 创建只有个人C端签署, 签署人需要人脸校验认证的合同流程**

1.只有一个个人C端参与人 (Approvers只有一个ApproverInfo元素)
2.签署区的指定通过绝对定位表达 (SignComponents中Component元素指定具体ComponentHeight/ComponentWidth/ComponentPosX/ComponentPosY/ComponentPage的方式)
3.C端参与人只有一个签名签署控件(SignComponents只有一个Component元素, 且这个元素的ComponentType是SIGN_SIGNATURE)
4.C端签署人需要人脸校验来签署合同 (ApproverSignTypes属性设置成[1]表示只能通过人脸识别校验来签署合同)

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId 110101200610116558 \
    --FlowName 西瓜采购协议(16:18:47) \
    --FlowApprovers.0.Name 张三 \
    --FlowApprovers.0.Mobile 18888888888 \
    --FlowApprovers.0.ApproverType PERSON \
    --FlowApprovers.0.ApproverSignTypes 1 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 112 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 40 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 146.15625 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 472.78125 \
    --FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FileIds yDSLoUUckpob089cUxVoXTn9T1cRb8W7 \
    --Unordered True \
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
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhii1vUyngyQvwQVL5QVup",
                "SignId": "yDCm3UUckpuhii1tUyngyQvupb93iMFu"
            }
        ],
        "FlowId": "yDCm3UUckpuhii1aUyngyQvu5Rn80ewb",
        "RequestId": "s1726295273067158522"
    }
}
```

**Example 10: 文件发起B2C合同，发起方设置合同水印（自定义水印内容）**

1.通过PDF文件发起合同 
2.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】 
3.指定C端签署方为个人【张三】 
4.水印控件通过外层 参数 Components 传递，ComponentType 设置为 WATERMARK，设置"ComponentExtra": "{\"Font\":\"黑体\",\"FontSize\":20,\"Opacity\":0.1,\"Density\":2,\"SubType\":\"CUSTOM_WATERMARK\"}"，ComponentValue 为自定义水印的内容

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --FlowName 文件发起B2C-自定义水印内容 \
    --Components.0.ComponentType WATERMARK \
    --Components.0.ComponentName 合同水印 \
    --Components.0.ComponentExtra {"Font":"黑体","FontSize":20,"Opacity":0.1,"Density":2,"SubType":"CUSTOM_WATERMARK"} \
    --Components.0.ComponentValue 自定义水印内容 \
    --Components.0.ComponentPage 0 \
    --Components.0.ComponentWidth 0 \
    --Components.0.ComponentHeight 0 \
    --Components.0.ComponentPosX 0 \
    --Components.0.ComponentPosY 0 \
    --Components.0.FileIndex 0 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.NotifyType NONE \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 119 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 7 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 143.59375 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 169.0625 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.Components.0.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-CREDIT-CODE","FontColor":"0,82,217"} \
    --FlowApprovers.0.Components.0.ComponentHeight 20 \
    --FlowApprovers.0.Components.0.ComponentPage 1 \
    --FlowApprovers.0.Components.0.ComponentPosX 205 \
    --FlowApprovers.0.Components.0.ComponentPosY 114 \
    --FlowApprovers.0.Components.0.ComponentRequired True \
    --FlowApprovers.0.Components.0.ComponentType TEXT \
    --FlowApprovers.0.Components.0.ComponentWidth 339 \
    --FlowApprovers.0.Components.0.FileIndex 0 \
    --FlowApprovers.0.Components.1.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-CREDIT-CODE"} \
    --FlowApprovers.0.Components.1.ComponentHeight 20 \
    --FlowApprovers.0.Components.1.ComponentPage 1 \
    --FlowApprovers.0.Components.1.ComponentPosX 234 \
    --FlowApprovers.0.Components.1.ComponentPosY 142 \
    --FlowApprovers.0.Components.1.ComponentRequired True \
    --FlowApprovers.0.Components.1.ComponentType TEXT \
    --FlowApprovers.0.Components.1.ComponentWidth 302 \
    --FlowApprovers.0.Components.1.FileIndex 0 \
    --FlowApprovers.0.Components.2.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"BUSI-LEGAL-NAME"} \
    --FlowApprovers.0.Components.2.ComponentHeight 20 \
    --FlowApprovers.0.Components.2.ComponentPage 1 \
    --FlowApprovers.0.Components.2.ComponentPosX 191.09 \
    --FlowApprovers.0.Components.2.ComponentPosY 172 \
    --FlowApprovers.0.Components.2.ComponentRequired True \
    --FlowApprovers.0.Components.2.ComponentType TEXT \
    --FlowApprovers.0.Components.2.ComponentWidth 335 \
    --FlowApprovers.0.Components.2.FileIndex 0 \
    --FlowApprovers.0.Components.3.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --FlowApprovers.0.Components.3.ComponentHeight 21 \
    --FlowApprovers.0.Components.3.ComponentPage 1 \
    --FlowApprovers.0.Components.3.ComponentPosX 155 \
    --FlowApprovers.0.Components.3.ComponentPosY 205 \
    --FlowApprovers.0.Components.3.ComponentRequired True \
    --FlowApprovers.0.Components.3.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.0.Components.3.ComponentWidth 366 \
    --FlowApprovers.0.Components.3.FileIndex 0 \
    --FlowApprovers.0.Components.4.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-NAME"} \
    --FlowApprovers.0.Components.4.ComponentHeight 20 \
    --FlowApprovers.0.Components.4.ComponentPage 1 \
    --FlowApprovers.0.Components.4.ComponentPosX 107 \
    --FlowApprovers.0.Components.4.ComponentPosY 236 \
    --FlowApprovers.0.Components.4.ComponentRequired True \
    --FlowApprovers.0.Components.4.ComponentType TEXT \
    --FlowApprovers.0.Components.4.ComponentWidth 339 \
    --FlowApprovers.0.Components.4.FileIndex 0 \
    --FlowApprovers.0.Components.5.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-MOBILE"} \
    --FlowApprovers.0.Components.5.ComponentHeight 20 \
    --FlowApprovers.0.Components.5.ComponentPage 1 \
    --FlowApprovers.0.Components.5.ComponentPosX 121 \
    --FlowApprovers.0.Components.5.ComponentPosY 265 \
    --FlowApprovers.0.Components.5.ComponentRequired True \
    --FlowApprovers.0.Components.5.ComponentType TEXT \
    --FlowApprovers.0.Components.5.ComponentWidth 327 \
    --FlowApprovers.0.Components.5.FileIndex 0 \
    --FlowApprovers.0.Components.6.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --FlowApprovers.0.Components.6.ComponentHeight 20 \
    --FlowApprovers.0.Components.6.ComponentPage 1 \
    --FlowApprovers.0.Components.6.ComponentPosX 35.09 \
    --FlowApprovers.0.Components.6.ComponentPosY 293 \
    --FlowApprovers.0.Components.6.ComponentRequired True \
    --FlowApprovers.0.Components.6.ComponentType DISTRICT \
    --FlowApprovers.0.Components.6.ComponentWidth 306 \
    --FlowApprovers.0.Components.6.FileIndex 0 \
    --FlowApprovers.0.Components.7.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --FlowApprovers.0.Components.7.ComponentHeight 44 \
    --FlowApprovers.0.Components.7.ComponentPage 1 \
    --FlowApprovers.0.Components.7.ComponentPosX 44 \
    --FlowApprovers.0.Components.7.ComponentPosY 652 \
    --FlowApprovers.0.Components.7.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.0.Components.7.ComponentWidth 505 \
    --FlowApprovers.0.Components.7.FileIndex 0 \
    --FlowApprovers.0.Components.8.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","ManualFill":true} \
    --FlowApprovers.0.Components.8.ComponentHeight 20 \
    --FlowApprovers.0.Components.8.ComponentPage 2 \
    --FlowApprovers.0.Components.8.ComponentPosX 145 \
    --FlowApprovers.0.Components.8.ComponentPosY 68 \
    --FlowApprovers.0.Components.8.ComponentRequired True \
    --FlowApprovers.0.Components.8.ComponentType DATE \
    --FlowApprovers.0.Components.8.ComponentWidth 116 \
    --FlowApprovers.0.Components.8.FileIndex 0 \
    --FlowApprovers.0.Components.9.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","ManualFill":true} \
    --FlowApprovers.0.Components.9.ComponentHeight 20 \
    --FlowApprovers.0.Components.9.ComponentPage 2 \
    --FlowApprovers.0.Components.9.ComponentPosX 130.09375 \
    --FlowApprovers.0.Components.9.ComponentPosY 555.09375 \
    --FlowApprovers.0.Components.9.ComponentType DATE \
    --FlowApprovers.0.Components.9.ComponentWidth 116 \
    --FlowApprovers.0.Components.9.FileIndex 0 \
    --FlowApprovers.0.Components.10.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --FlowApprovers.0.Components.10.ComponentHeight 27 \
    --FlowApprovers.0.Components.10.ComponentPage 2 \
    --FlowApprovers.0.Components.10.ComponentPosX 134.09 \
    --FlowApprovers.0.Components.10.ComponentPosY 628.09 \
    --FlowApprovers.0.Components.10.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.0.Components.10.ComponentWidth 398 \
    --FlowApprovers.0.Components.10.FileIndex 0 \
    --FlowApprovers.0.Components.11.ComponentExtra {} \
    --FlowApprovers.0.Components.11.ComponentHeight 16 \
    --FlowApprovers.0.Components.11.ComponentPage 7 \
    --FlowApprovers.0.Components.11.ComponentPosX 83.09375 \
    --FlowApprovers.0.Components.11.ComponentPosY 96.5625 \
    --FlowApprovers.0.Components.11.ComponentType CHECK_BOX \
    --FlowApprovers.0.Components.11.ComponentWidth 16 \
    --FlowApprovers.0.Components.11.FileIndex 0 \
    --FlowApprovers.0.Components.12.ComponentExtra {"FillMethod":0,"NotMakeImageCenter":true} \
    --FlowApprovers.0.Components.12.ComponentHeight 119 \
    --FlowApprovers.0.Components.12.ComponentPage 7 \
    --FlowApprovers.0.Components.12.ComponentPosX 13 \
    --FlowApprovers.0.Components.12.ComponentPosY 394 \
    --FlowApprovers.0.Components.12.ComponentType FILL_IMAGE \
    --FlowApprovers.0.Components.12.ComponentWidth 119 \
    --FlowApprovers.0.Components.12.FileIndex 0 \
    --FlowApprovers.0.Components.13.ComponentExtra {"LimitCount":3,"AttachmentType":"IMG"} \
    --FlowApprovers.0.Components.13.ComponentHeight 42 \
    --FlowApprovers.0.Components.13.ComponentPage 7 \
    --FlowApprovers.0.Components.13.ComponentPosX 12 \
    --FlowApprovers.0.Components.13.ComponentPosY 537 \
    --FlowApprovers.0.Components.13.ComponentRequired True \
    --FlowApprovers.0.Components.13.ComponentType ATTACHMENT \
    --FlowApprovers.0.Components.13.ComponentWidth 240 \
    --FlowApprovers.0.Components.13.FileIndex 0 \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.Name 张三 \
    --FlowApprovers.1.Mobile 18888888888 \
    --FlowApprovers.1.NotifyType NONE \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 43 \
    --FlowApprovers.1.SignComponents.0.ComponentPage 7 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 433.59375 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 196.0625 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 119 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.Components.0.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-NAME"} \
    --FlowApprovers.1.Components.0.ComponentHeight 20 \
    --FlowApprovers.1.Components.0.ComponentPage 1 \
    --FlowApprovers.1.Components.0.ComponentPosX 199 \
    --FlowApprovers.1.Components.0.ComponentPosY 323 \
    --FlowApprovers.1.Components.0.ComponentRequired True \
    --FlowApprovers.1.Components.0.ComponentType TEXT \
    --FlowApprovers.1.Components.0.ComponentWidth 309 \
    --FlowApprovers.1.Components.0.FileIndex 0 \
    --FlowApprovers.1.Components.1.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"LOCATION"} \
    --FlowApprovers.1.Components.1.ComponentHeight 24 \
    --FlowApprovers.1.Components.1.ComponentPage 1 \
    --FlowApprovers.1.Components.1.ComponentPosX 155 \
    --FlowApprovers.1.Components.1.ComponentPosY 386 \
    --FlowApprovers.1.Components.1.ComponentRequired True \
    --FlowApprovers.1.Components.1.ComponentType MULTI_LINE_TEXT \
    --FlowApprovers.1.Components.1.ComponentWidth 390 \
    --FlowApprovers.1.Components.1.FileIndex 0 \
    --FlowApprovers.1.Components.2.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体"} \
    --FlowApprovers.1.Components.2.ComponentHeight 20 \
    --FlowApprovers.1.Components.2.ComponentPage 1 \
    --FlowApprovers.1.Components.2.ComponentPosX 114.09 \
    --FlowApprovers.1.Components.2.ComponentPosY 416 \
    --FlowApprovers.1.Components.2.ComponentRequired True \
    --FlowApprovers.1.Components.2.ComponentType TEXT \
    --FlowApprovers.1.Components.2.ComponentWidth 299 \
    --FlowApprovers.1.Components.2.FileIndex 0 \
    --FlowApprovers.1.Components.3.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","RecipientInfoType":"PERSONAL-MOBILE"} \
    --FlowApprovers.1.Components.3.ComponentHeight 20 \
    --FlowApprovers.1.Components.3.ComponentPage 1 \
    --FlowApprovers.1.Components.3.ComponentPosX 115.09 \
    --FlowApprovers.1.Components.3.ComponentPosY 445 \
    --FlowApprovers.1.Components.3.ComponentRequired True \
    --FlowApprovers.1.Components.3.ComponentType TEXT \
    --FlowApprovers.1.Components.3.ComponentWidth 367 \
    --FlowApprovers.1.Components.3.FileIndex 0 \
    --FlowApprovers.1.Components.4.ComponentExtra {"SubType":"EDUCATION"} \
    --FlowApprovers.1.Components.4.ComponentHeight 20 \
    --FlowApprovers.1.Components.4.ComponentId ComponentId_30 \
    --FlowApprovers.1.Components.4.ComponentName 学历 \
    --FlowApprovers.1.Components.4.ComponentPage 1 \
    --FlowApprovers.1.Components.4.ComponentPosX 8.09375 \
    --FlowApprovers.1.Components.4.ComponentPosY 473 \
    --FlowApprovers.1.Components.4.ComponentRequired True \
    --FlowApprovers.1.Components.4.ComponentType SELECTOR \
    --FlowApprovers.1.Components.4.ComponentWidth 84 \
    --FlowApprovers.1.Components.4.FileIndex 0 \
    --FlowApprovers.1.Components.5.ComponentExtra {"FontSize":12,"FontAlign":"Left","Font":"黑体","SubType":"EMAIL"} \
    --FlowApprovers.1.Components.5.ComponentHeight 20 \
    --FlowApprovers.1.Components.5.ComponentId ComponentId_28 \
    --FlowApprovers.1.Components.5.ComponentName 邮箱 \
    --FlowApprovers.1.Components.5.ComponentPage 1 \
    --FlowApprovers.1.Components.5.ComponentPosX 117.09375 \
    --FlowApprovers.1.Components.5.ComponentPosY 474 \
    --FlowApprovers.1.Components.5.ComponentType TEXT \
    --FlowApprovers.1.Components.5.ComponentWidth 292 \
    --FlowApprovers.1.Components.5.FileIndex 0 \
    --FlowApprovers.1.Components.6.ComponentExtra {"SubType":"GENDER"} \
    --FlowApprovers.1.Components.6.ComponentHeight 20 \
    --FlowApprovers.1.Components.6.ComponentId ComponentId_29 \
    --FlowApprovers.1.Components.6.ComponentName 性别 \
    --FlowApprovers.1.Components.6.ComponentPage 1 \
    --FlowApprovers.1.Components.6.ComponentPosX 424.09375 \
    --FlowApprovers.1.Components.6.ComponentPosY 472 \
    --FlowApprovers.1.Components.6.ComponentRequired True \
    --FlowApprovers.1.Components.6.ComponentType SELECTOR \
    --FlowApprovers.1.Components.6.ComponentWidth 84 \
    --FlowApprovers.1.Components.6.FileIndex 0 \
    --FileIds yDCWqUUckpve5id3U4f5EL77tlNh6zTZ
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiir7UyngyQv8jrtNLw6f",
                "SignId": "yDCm3UUckpuhiir4UyngyQv1cGEVXL3w"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiiruUyngyQvdLX3DRJK7",
                "SignId": "yDCm3UUckpuhiirbUyngyQvpaOBqrvlD"
            }
        ],
        "FlowId": "yDCm3UUckpuhiirxUyngyQv1srq0CaC8",
        "RequestId": "s1726295754261345096"
    }
}
```

**Example 11: 文件发起 签署方含有签批控件**

1.通过PDF文件发起合同 
2.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】 
3.指定C端签署方为个人【张三】 
4.B 端签署人 有两个签署控件， 分别是签名控件和签批控件(SIGN_VIRTUAL_COMBINATION)，其中签批控件包含四个子控件, 在 Component 中的  "ComponentExtra": "{\"Children\":[\"ComponentId_29\",\"ComponentId_27\",\"ComponentId_28\",\"ComponentId_30\"]}" 体现 ， 包括 审批意见(SIGN_SELECTOR)，个人签名(SIGN_SIGNATURE)，签署日期(SIGN_DATE)，批注附言(SIGN_MULTI_LINE_TEXT)
5.C 端签署人 有一个签批控件(SIGN_VIRTUAL_COMBINATION)，其中签批控件包含三个子控件, 在 Component 中的  "ComponentExtra": "{\"Children\":[\"ComponentId_19\",\"ComponentId_17\",\"ComponentId_18\"]}" 体现 ， 包括 审批意见(SIGN_SELECTOR)，个人签名(SIGN_SIGNATURE)，签署日期(SIGN_DATE)

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --FlowName 文件发起-签批 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.SignComponents.0.ComponentId ComponentId_1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 160 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowApprovers.0.SignComponents.1.ComponentId ComponentId_2 \
    --FlowApprovers.0.SignComponents.1.ComponentPosY 360 \
    --FlowApprovers.0.SignComponents.1.ComponentWidth 100 \
    --FlowApprovers.0.SignComponents.1.FileIndex 0 \
    --FlowApprovers.0.SignComponents.1.ComponentType SIGN_DATE \
    --FlowApprovers.0.SignComponents.1.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.1.ComponentPosX 160 \
    --FlowApprovers.0.SignComponents.1.ComponentHeight 50 \
    --FlowApprovers.0.SignComponents.2.ComponentExtra {"Children":["ComponentId_29","ComponentId_27","ComponentId_28","ComponentId_30"]} \
    --FlowApprovers.0.SignComponents.2.ComponentHeight 211 \
    --FlowApprovers.0.SignComponents.2.ComponentId ComponentId_26 \
    --FlowApprovers.0.SignComponents.2.ComponentName 签批1 \
    --FlowApprovers.0.SignComponents.2.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.2.ComponentPosX 180 \
    --FlowApprovers.0.SignComponents.2.ComponentPosY 478 \
    --FlowApprovers.0.SignComponents.2.ComponentType SIGN_VIRTUAL_COMBINATION \
    --FlowApprovers.0.SignComponents.2.ComponentWidth 210 \
    --FlowApprovers.0.SignComponents.2.ComponentRequired False \
    --FlowApprovers.0.SignComponents.3.ComponentExtra {"Values":["审批通过","审批不通过"],"FontSize":12,"FontAlign":"Left","Font":"黑体","MultiSelect":false} \
    --FlowApprovers.0.SignComponents.3.ComponentHeight 20 \
    --FlowApprovers.0.SignComponents.3.ComponentId ComponentId_29 \
    --FlowApprovers.0.SignComponents.3.ComponentName 审批意见 \
    --FlowApprovers.0.SignComponents.3.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.3.ComponentPosX 180 \
    --FlowApprovers.0.SignComponents.3.ComponentPosY 567 \
    --FlowApprovers.0.SignComponents.3.ComponentRequired True \
    --FlowApprovers.0.SignComponents.3.ComponentType SIGN_SELECTOR \
    --FlowApprovers.0.SignComponents.3.ComponentWidth 210 \
    --FlowApprovers.0.SignComponents.4.ComponentExtra {"Date":true,"isAfterCut":true} \
    --FlowApprovers.0.SignComponents.4.ComponentHeight 43 \
    --FlowApprovers.0.SignComponents.4.ComponentId ComponentId_27 \
    --FlowApprovers.0.SignComponents.4.ComponentName 个人签名/印章 \
    --FlowApprovers.0.SignComponents.4.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.4.ComponentPosX 185 \
    --FlowApprovers.0.SignComponents.4.ComponentPosY 478 \
    --FlowApprovers.0.SignComponents.4.ComponentRequired True \
    --FlowApprovers.0.SignComponents.4.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.4.ComponentWidth 119 \
    --FlowApprovers.0.SignComponents.5.ComponentExtra {"Format":"yyyy年m月d日","Gaps":"2,2","FontSize":12,"FontAlign":"Center","Font":"黑体","isAfterCut":true} \
    --FlowApprovers.0.SignComponents.5.ComponentHeight 20 \
    --FlowApprovers.0.SignComponents.5.ComponentId ComponentId_28 \
    --FlowApprovers.0.SignComponents.5.ComponentName 签署日期 \
    --FlowApprovers.0.SignComponents.5.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.5.ComponentPosX 185 \
    --FlowApprovers.0.SignComponents.5.ComponentPosY 541 \
    --FlowApprovers.0.SignComponents.5.ComponentRequired True \
    --FlowApprovers.0.SignComponents.5.ComponentType SIGN_DATE \
    --FlowApprovers.0.SignComponents.5.ComponentWidth 119 \
    --FlowApprovers.0.SignComponents.6.ComponentExtra {"FontSize":12,"FontAlign":"Left","VerticalAlign":"Top","Font":"黑体"} \
    --FlowApprovers.0.SignComponents.6.ComponentHeight 54 \
    --FlowApprovers.0.SignComponents.6.ComponentId ComponentId_30 \
    --FlowApprovers.0.SignComponents.6.ComponentName 批注附言 \
    --FlowApprovers.0.SignComponents.6.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.6.ComponentPosX 180 \
    --FlowApprovers.0.SignComponents.6.ComponentPosY 635 \
    --FlowApprovers.0.SignComponents.6.ComponentRequired True \
    --FlowApprovers.0.SignComponents.6.ComponentType SIGN_MULTI_LINE_TEXT \
    --FlowApprovers.0.SignComponents.6.ComponentWidth 210 \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.Name 张三 \
    --FlowApprovers.1.Mobile 18888888888 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 160 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FlowApprovers.1.SignComponents.1.ComponentExtra {"Children":["ComponentId_19","ComponentId_17","ComponentId_18"]} \
    --FlowApprovers.1.SignComponents.1.ComponentHeight 211 \
    --FlowApprovers.1.SignComponents.1.ComponentId ComponentId_16 \
    --FlowApprovers.1.SignComponents.1.ComponentName 签批1 \
    --FlowApprovers.1.SignComponents.1.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.1.ComponentPosX 280 \
    --FlowApprovers.1.SignComponents.1.ComponentPosY 478 \
    --FlowApprovers.1.SignComponents.1.ComponentType SIGN_VIRTUAL_COMBINATION \
    --FlowApprovers.1.SignComponents.1.ComponentWidth 210 \
    --FlowApprovers.1.SignComponents.2.ComponentExtra {"Values":["审批通过","审批不通过"],"FontSize":12,"FontAlign":"Left","Font":"黑体","MultiSelect":false} \
    --FlowApprovers.1.SignComponents.2.ComponentHeight 20 \
    --FlowApprovers.1.SignComponents.2.ComponentId ComponentId_19 \
    --FlowApprovers.1.SignComponents.2.ComponentName 审批意见 \
    --FlowApprovers.1.SignComponents.2.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.2.ComponentPosX 280 \
    --FlowApprovers.1.SignComponents.2.ComponentPosY 567 \
    --FlowApprovers.1.SignComponents.2.ComponentRequired True \
    --FlowApprovers.1.SignComponents.2.ComponentType SIGN_SELECTOR \
    --FlowApprovers.1.SignComponents.2.ComponentWidth 210 \
    --FlowApprovers.1.SignComponents.3.ComponentExtra {"Format":"yyyy年m月d日","Gaps":"2,2","FontSize":12,"FontAlign":"Center","Font":"黑体","isAfterCut":true} \
    --FlowApprovers.1.SignComponents.3.ComponentHeight 20 \
    --FlowApprovers.1.SignComponents.3.ComponentId ComponentId_18 \
    --FlowApprovers.1.SignComponents.3.ComponentName 签署日期 \
    --FlowApprovers.1.SignComponents.3.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.3.ComponentPosX 285 \
    --FlowApprovers.1.SignComponents.3.ComponentPosY 541 \
    --FlowApprovers.1.SignComponents.3.ComponentRequired True \
    --FlowApprovers.1.SignComponents.3.ComponentType SIGN_DATE \
    --FlowApprovers.1.SignComponents.3.ComponentWidth 119 \
    --FlowApprovers.1.SignComponents.4.ComponentExtra {"Date":true,"isAfterCut":true} \
    --FlowApprovers.1.SignComponents.4.ComponentHeight 43 \
    --FlowApprovers.1.SignComponents.4.ComponentId ComponentId_17 \
    --FlowApprovers.1.SignComponents.4.ComponentName 个人签名/印章 \
    --FlowApprovers.1.SignComponents.4.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.4.ComponentPosX 285 \
    --FlowApprovers.1.SignComponents.4.ComponentPosY 478 \
    --FlowApprovers.1.SignComponents.4.ComponentRequired True \
    --FlowApprovers.1.SignComponents.4.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.1.SignComponents.4.ComponentWidth 119 \
    --FileIds yDCWqUUckpve5id3U4f5EL77tlNh6zTZ \
    --Unordered True
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiiwrUyngyQvEAAG8aSuj",
                "SignId": "yDCm3UUckpuhiiwlUyngyQvEVt11WQd6"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCm3UUckpuhiiw5UyngyQvvbypsA2N5",
                "SignId": "yDCm3UUckpuhiiw0UyngyQvxIu5Rvq2L"
            }
        ],
        "FlowId": "yDCm3UUckpuhiiw2UyngyQv8OPSX8qYD",
        "RequestId": "s1726284341125380532"
    }
}
```

**Example 12: 文件发起 使用关键字定位 签署方含有签批控件**

注意： 关键字定位的签批控件，子控件的位置，大小是固定的，不能自定义。
1.通过PDF文件发起合同 
2.使用的是关键字定位
3.指定B端签署方为企业【典子谦示例企业】，经办人为【典子谦】 
4.指定C端签署方为个人【张三】 
5.B 端签署人 有两个签署控件， 分别是签名控件和签批控件(SIGN_VIRTUAL_COMBINATION)，其中签批控件包含四个子控件, 在 Component 中的  "ComponentExtra": "{\"ChildrenTypes\":[\"SIGN_SIGNATURE\",\"SIGN_DATE\",\"SIGN_SELECTOR\",\"SIGN_MULTI_LINE_TEXT\"]}" 体现 ， 包括 审批意见(SIGN_SELECTOR)，个人签名(SIGN_SIGNATURE)，签署日期(SIGN_DATE)，批注附言(SIGN_MULTI_LINE_TEXT)， 但是关键字跟绝对定位的区别在于 关键字方式只用传递SIGN_VIRTUAL_COMBINATION 一个签署控件即可
6.C 端签署人 有一个签批控件(SIGN_VIRTUAL_COMBINATION)，其中签批控件包含三个子控件, 在 Component 中的   "ComponentExtra": "{\"ChildrenTypes\":[\"SIGN_SIGNATURE\",\"SIGN_DATE\",\"SIGN_SELECTOR\",\"SIGN_MULTI_LINE_TEXT\"]}" 体现 ， 包括 审批意见(SIGN_SELECTOR)，个人签名(SIGN_SIGNATURE)，签署日期(SIGN_DATE)， 但是关键字跟绝对定位的区别在于 关键字方式只用传递SIGN_VIRTUAL_COMBINATION 一个签署控件即可

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --FlowName 文件发起-签批 \
    --FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowApprovers.0.OrganizationOpenId org_dianziqian \
    --FlowApprovers.0.OpenId n9527 \
    --FlowApprovers.0.Name 典子谦 \
    --FlowApprovers.0.Mobile 13200000000 \
    --FlowApprovers.0.OrganizationName 典子谦示例企业 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.GenerateMode KEYWORD \
    --FlowApprovers.0.SignComponents.0.OffsetX 0 \
    --FlowApprovers.0.SignComponents.0.OffsetY 0 \
    --FlowApprovers.0.SignComponents.0.RelativeLocation Right \
    --FlowApprovers.0.SignComponents.0.ComponentId Test1 \
    --FlowApprovers.0.SignComponents.0.ComponentExtra {"ChildrenTypes":["SIGN_SIGNATURE","SIGN_DATE","SIGN_SELECTOR","SIGN_MULTI_LINE_TEXT"]} \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 234 \
    --FlowApprovers.0.SignComponents.0.ComponentName 签批1 \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_VIRTUAL_COMBINATION \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 210 \
    --FlowApprovers.0.SignComponents.0.ComponentRequired False \
    --FlowApprovers.1.ApproverType PERSON \
    --FlowApprovers.1.Name 张三 \
    --FlowApprovers.1.Mobile 18888888888 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.GenerateMode KEYWORD \
    --FlowApprovers.1.SignComponents.0.OffsetX 0 \
    --FlowApprovers.1.SignComponents.0.OffsetY 0 \
    --FlowApprovers.1.SignComponents.0.RelativeLocation Right \
    --FlowApprovers.1.SignComponents.0.ComponentId Test2 \
    --FlowApprovers.1.SignComponents.0.ComponentExtra {"ChildrenTypes":["SIGN_SIGNATURE","SIGN_DATE","SIGN_SELECTOR","SIGN_MULTI_LINE_TEXT"]} \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 234 \
    --FlowApprovers.1.SignComponents.0.ComponentName 签批1 \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_VIRTUAL_COMBINATION \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 210 \
    --FlowApprovers.1.SignComponents.0.ComponentRequired False \
    --FileIds yDCWqUUckpve5id3U4f5EL77tlNh6zTZ \
    --Unordered True
```

Output: 
```
{
    "Response": {
        "Approvers": [
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCdoUUckp7ltep9Uyq2ikIypsCCIqXS",
                "SignId": "yDCdoUUckp7ltepxUyq2ikIE79iVjD2I"
            },
            {
                "ApproverRoleName": "",
                "RecipientId": "yDCdoUUckp7ltep7Uyq2ikIuzVkVXNut",
                "SignId": "yDCdoUUckp7ltep4Uyq2ikI1baBbI9zJ"
            }
        ],
        "FlowId": "yDCdoUUckp7ltepfUyq2ikI8VC2s92zT",
        "RequestId": "s1732015258075060878"
    }
}
```

