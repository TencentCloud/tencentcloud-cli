**Example 1: 使用模板批量创建流程**



Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowInfos.0.FlowName 测试流程一 \
    --FlowInfos.0.TemplateId 005c7f6b062a70e0c3982c84f7f64e8c \
    --FlowInfos.0.FlowDescription 测试流程一的描述信息 \
    --FlowInfos.0.FlowType 合同 \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.CallbackUrl  \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.Name 李四 \
    --FlowInfos.0.FlowApprovers.0.Mobile 13888888888 \
    --FlowInfos.0.FlowApprovers.0.Deadline 1604910798 \
    --FlowInfos.1.FlowName 测试流程二 \
    --FlowInfos.1.TemplateId 005c7f6b062a70e0c398ejoqwnrf4e8c \
    --FlowInfos.1.FlowDescription 测试流程二的描述信息 \
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
            "yDxMqUyKQDAIJ2UuO4zjE1trvvaigGvi",
            "yDxMqUyKQDAIJ2UuO4zjE1trvvaigGv2"
        ],
        "PreviewUrls": [
            "",
            ""
        ],
        "ErrorMessages": [
            "",
            ""
        ],
        "RequestId": "s1629442787650001803"
    }
}
```

**Example 2: B2B 模板发起示例**

双方企业均认证 发起示例

Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowInfos.0.FlowName 测试流程一 \
    --FlowInfos.0.TemplateId 005c7f6b062a70e0c3982c84f7f64e8c \
    --FlowInfos.0.FlowDescription 测试流程一的描述信息 \
    --FlowInfos.0.FlowType 合同 \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.CallbackUrl  \
    --FlowInfos.0.FormFields.0.ComponentName 姓名 \
    --FlowInfos.0.FormFields.0.ComponentValue 李四 \
    --FlowInfos.0.FlowApprovers.0.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.0.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --FlowInfos.0.FlowApprovers.0.RecipientId yDxjbUUgydjm5r95UuO4zjEuCkSaxt8n \
    --FlowInfos.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.1.OpenId eezi_openid \
    --FlowInfos.0.FlowApprovers.1.OrganizationOpenId organization1_open_id \
    --FlowInfos.0.FlowApprovers.1.OrganizationName 鹅鹅子的企业 \
    --FlowInfos.0.FlowApprovers.1.RecipientId yDxjbUUgydjm52hzUuO4zjEChJBkK7qS
```

Output: 
```
{
    "Response": {
        "CustomerData": [
            ""
        ],
        "FlowIds": [
            "yDxMqUyKQDAIJ2UuO4zjE1trvvaigGvi"
        ],
        "PreviewUrls": [
            ""
        ],
        "ErrorMessages": [
            ""
        ],
        "RequestId": "s1629442787650001803"
    }
}
```

