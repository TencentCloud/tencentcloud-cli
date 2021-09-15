**Example 1: 使用模板批量创建流程**



Input: 

```
tccli essbasic CreateFlowsByTemplates --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.CustomUserId xx \
    --Operator.ProxyIp xx \
    --Operator.Channel xx \
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
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.TemplateId xx \
    --FlowInfos.0.FlowType xx \
    --FlowInfos.0.CallbackUrl xx \
    --FlowInfos.1.FlowName xx \
    --FlowInfos.1.FlowDescription xx \
    --FlowInfos.1.FormFields.0.ComponentName xx \
    --FlowInfos.1.FormFields.0.ComponentValue xx \
    --FlowInfos.1.FormFields.0.ComponentId xx \
    --FlowInfos.1.CustomerData xx \
    --FlowInfos.1.FlowApprovers.0.Name xx \
    --FlowInfos.1.FlowApprovers.0.Mobile xx \
    --FlowInfos.1.FlowApprovers.0.JumpUrl xx \
    --FlowInfos.1.FlowApprovers.0.Deadline 0 \
    --FlowInfos.1.FlowApprovers.0.IdCardNumber xx \
    --FlowInfos.1.FlowApprovers.0.CallbackUrl xx \
    --FlowInfos.1.Deadline 1604910797 \
    --FlowInfos.1.TemplateId xx \
    --FlowInfos.1.FlowType xx \
    --FlowInfos.1.CallbackUrl xx \
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
        "CustomerData": [
            "",
            ""
        ],
        "FlowIds": [
            "yDxMqUyKQDAIJ2UuO4zjE1trvvaigGvi",
            "yDxMqUyKQDAIJ2UuO4zjE1trvvaigGv2"
        ],
        "ErrorMessages": [
            "",
            ""
        ],
        "RequestId": "s1629442787650001803"
    }
}
```

