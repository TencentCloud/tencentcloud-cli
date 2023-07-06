**Example 1: 通过多文件创建合同组签署流程**

通过多文件创建合同组签署流程

Input: 

```
tccli essbasic ChannelCreateFlowGroupByFiles --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.AppId test \
    --FlowGroupName testx \
    --ApproverVerifyType VerifyCheck \
    --FlowFileInfos.0.FlowName  \
    --FlowFileInfos.0.FlowApprovers.0.ApproverType testx \
    --FlowFileInfos.0.FlowApprovers.0.OrganizationName testx \
    --FlowFileInfos.0.FlowApprovers.0.OrganizationOpenId testx \
    --FlowFileInfos.0.FlowApprovers.0.OpenId testx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.GenerateMode testx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentName testx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentType testx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.GenerateMode testx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.ComponentName testx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.FileIndex 0 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.ComponentType testx \
    --FlowFileInfos.0.FileIds testx
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "test",
        "FlowIds": [
            "test",
            "test"
        ],
        "RequestId": "test"
    }
}
```

