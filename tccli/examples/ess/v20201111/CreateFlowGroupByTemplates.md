**Example 1: 合同组示例**

合同组发起示例,此示例, 第一份子合同 为单个自动签
第二份子合同为B2C自动签, 其中B端为自动签
第三份子合同为B2B 经办签署

Input: 

```
tccli ess CreateFlowGroupByTemplates --cli-unfold-argument  \
    --Operator.UserId ***************** \
    --FlowGroupName 合同组自动签模板发起 \
    --FlowGroupInfos.0.TemplateId ********** \
    --FlowGroupInfos.0.FlowName 单B自动签 \
    --FlowGroupInfos.0.FlowType 合同组 \
    --FlowGroupInfos.0.FlowDescription 单B自动签 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 3 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 发起方公司名称 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 本方发起人 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 本方发起人电话 \
    --FlowGroupInfos.0.Unordered False \
    --FlowGroupInfos.1.TemplateId yDwXJ************************ZMMtV \
    --FlowGroupInfos.1.FlowName 自动签B2C \
    --FlowGroupInfos.1.FlowType 合同组 \
    --FlowGroupInfos.1.FlowDescription 自动签B2C \
    --FlowGroupInfos.1.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 发起方公司名称 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 本方发起人 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 本方发起人电话 \
    --FlowGroupInfos.1.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 个人签署人 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 个人签署人电话 \
    --FlowGroupInfos.2.TemplateId yDw**********************nGBhHG \
    --FlowGroupInfos.2.FlowName B2B手动签 \
    --FlowGroupInfos.2.FlowType 合同组 \
    --FlowGroupInfos.2.FlowDescription B2B手动签 \
    --FlowGroupInfos.2.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.2.Approvers.0.OrganizationName 经办人公司名称 \
    --FlowGroupInfos.2.Approvers.0.ApproverName 经办人 \
    --FlowGroupInfos.2.Approvers.0.ApproverMobile 经办人电话 \
    --FlowGroupInfos.2.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.2.Approvers.1.OrganizationName 签署方公司 \
    --FlowGroupInfos.2.Approvers.1.ApproverName 签署方经办人 \
    --FlowGroupInfos.2.Approvers.1.ApproverMobile 签署方经办人电话
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "********************",
        "FlowIds": [
            "*****************",
            "*****************",
            "*****************"
        ],
        "RequestId": "********"
    }
}
```

