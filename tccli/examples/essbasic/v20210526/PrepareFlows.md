**Example 1: 创建待发起文件**

创建待发起文件

Input: 

```
tccli essbasic PrepareFlows --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.AppId x \
    --JumpUrl http://www.test.com \
    --FlowInfos.0.FlowName 测试签署流程一 \
    --FlowInfos.0.TemplateId test \
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
    --FlowInfos.1.TemplateId test \
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
        "ConfirmUrl": "https://www.xx.com",
        "RequestId": "id"
    }
}
```

