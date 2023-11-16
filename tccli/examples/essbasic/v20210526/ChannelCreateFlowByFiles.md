**Example 1: 创建含有动态签署人流程，签署方不指定具体的签署人**

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

**Example 2: 使用文件创建B2B2C的合同**

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

**Example 3: 使用文件创建单自然人签署的合同**

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

