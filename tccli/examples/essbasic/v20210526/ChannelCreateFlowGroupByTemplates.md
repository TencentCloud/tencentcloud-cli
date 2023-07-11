**Example 1: 通过多模板创建合同组签署流程**

通过多模板创建合同组签署流程

Input: 

```
tccli essbasic ChannelCreateFlowGroupByTemplates --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.AppId test \
    --FlowGroupName testx \
    --FlowInfos.0.FlowName testx \
    --FlowInfos.0.TemplateId testx \
    --FlowInfos.0.FlowDescription testx \
    --FlowInfos.0.Deadline 1604910797 \
    --FlowInfos.0.CallbackUrl testx \
    --FlowInfos.0.FormFields.0.ComponentName testx \
    --FlowInfos.0.FormFields.0.ComponentValue testx \
    --FlowInfos.0.FlowApprovers.0.ApproverType PERSON \
    --FlowInfos.0.FlowApprovers.0.Name testx \
    --FlowInfos.0.FlowApprovers.0.Mobile testx \
    --FlowInfos.0.FlowApprovers.0.RecipientId testx \
    --FlowInfos.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowInfos.0.FlowApprovers.1.OpenId testx \
    --FlowInfos.0.FlowApprovers.1.OrganizationOpenId testx \
    --FlowInfos.0.FlowApprovers.1.OrganizationName testx \
    --FlowInfos.0.FlowApprovers.1.RecipientId testx
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "test",
        "FlowIds": [
            "test"
        ],
        "TaskInfos": [
            {
                "TaskId": "test",
                "TaskStatus": "test"
            }
        ],
        "RequestId": "test"
    }
}
```

