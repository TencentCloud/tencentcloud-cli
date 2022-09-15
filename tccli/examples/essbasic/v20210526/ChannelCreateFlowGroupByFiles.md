**Example 1: 通过多文件创建合同组签署流程**



Input: 

```
tccli essbasic ChannelCreateFlowGroupByFiles --cli-unfold-argument  \
    --Agent.ProxyAppId xxx \
    --Agent.ProxyOrganizationId xxx \
    --Agent.ProxyOrganizationOpenId xxx \
    --Agent.AppId xxx \
    --FlowGroupName xxx \
    --FlowFileInfos.0.FlowName  \
    --FlowFileInfos.0.FlowApprovers.0.ApproverType xxx \
    --FlowFileInfos.0.FlowApprovers.0.OrganizationName xxx \
    --FlowFileInfos.0.FlowApprovers.0.OrganizationOpenId xxx \
    --FlowFileInfos.0.FlowApprovers.0.OpenId xxx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.GenerateMode xxx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentName xxx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentType xxx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.GenerateMode xxx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.ComponentName xxx \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.FileIndex 0 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.1.ComponentType xxx \
    --FlowFileInfos.0.FileIds xxx
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "xx",
        "FlowIds": [
            "xx",
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

