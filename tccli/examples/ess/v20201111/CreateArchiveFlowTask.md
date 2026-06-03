**Example 1: 创建合同归档任务**



Input: 

```
tccli ess CreateArchiveFlowTask --cli-unfold-argument  \
    --Operator.UserId yDtT9UUckp*****************Q0bO6 \
    --ArchiveFlows.0.ResourceIds yD3hnUUck***************vmOnrcHE \
    --ArchiveFlows.0.FlowName 测试3-flow_name \
    --ArchiveFlows.0.FlowType 租房合同 \
    --ArchiveFlows.0.BusinessId 测试3-business_id \
    --ArchiveFlows.0.CreatorName 发起方 \
    --ArchiveFlows.0.ApproverInfo.0.ApproverName 李白 \
    --ArchiveFlows.0.ApproverInfo.0.ApproverType 1 \
    --ArchiveFlows.0.ApproverInfo.0.ApproverMobile 1763******1 \
    --ArchiveFlows.0.ApproverInfo.0.ApproverEmail 175******1@qq.com \
    --ArchiveFlows.0.ApproverInfo.0.ApproverIdCardType ID_CARD \
    --ArchiveFlows.0.ApproverInfo.0.ApproverIdCardNumber 4115************12 \
    --ArchiveFlows.0.ApproverInfo.0.ApproveTime 1779157787 \
    --ArchiveFlows.0.CcInfo.0.ApproverName 张三 \
    --ArchiveFlows.0.UserData 用户的自定义数据 \
    --ArchiveFlows.0.FlowDescription 这是合同描述 \
    --ArchiveFlows.0.ApproveTime 1779157787 \
    --ArchiveFlows.0.CustomCreatedOn 1779147787
```

Output: 
```
{
    "Response": {
        "TaskId": "yD3h6UUckpzjnz27UkwEdGoGm3LFAtgX",
        "RequestId": "1b9bbc05-1ed1-4c9d-914b-44e327d79e51"
    }
}
```

