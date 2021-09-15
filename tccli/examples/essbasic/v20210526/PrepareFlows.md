**Example 1: 创建待发起文件**



Input: 

```
tccli essbasic PrepareFlows --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.CustomUserId xx \
    --Operator.ProxyIp xx \
    --Operator.Channel xx \
    --JumpUrl xx \
    --FlowInfos.0.FlowName xx \
    --FlowInfos.0.FlowDescription xx \
    --FlowInfos.0.FormFields.0.ComponentName xx \
    --FlowInfos.0.FormFields.0.ComponentValue xx \
    --FlowInfos.0.FormFields.0.ComponentId xx \
    --FlowInfos.0.CustomerData xx \
    --FlowInfos.0.FlowApprovers.0.Name xx \
    --FlowInfos.0.FlowApprovers.0.Mobile xx \
    --FlowInfos.0.FlowApprovers.0.JumpUrl xx \
    --FlowInfos.0.FlowApprovers.0.Deadline 0 \
    --FlowInfos.0.FlowApprovers.0.IdCardNumber xx \
    --FlowInfos.0.FlowApprovers.0.CallbackUrl xx \
    --FlowInfos.0.Deadline 0 \
    --FlowInfos.0.TemplateId xx \
    --FlowInfos.0.FlowType xx \
    --FlowInfos.0.CallbackUrl xx \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.AppId xx
```

Output: 
```
{
    "Response": {
        "ConfirmUrl": "www.qq.com",
        "RequestId": "xx"
    }
}
```

