**Example 1: 更新合同备注**



Input: 

```
tccli ess OperateFlowRemarks --cli-unfold-argument  \
    --Operator.UserId yDCp0UUckpay74u2Uxgcd4v1197NeSXv \
    --FlowId yDt**************************wzZ \
    --OperateType UPDATE \
    --FlowItem.RemarkId 1 \
    --FlowItem.RemarkValue 新的标签 \
    --FlowGroupId yD3**************************CkC
```

Output: 
```
{
    "Response": {
        "RequestId": "5de73ff1-d7ab-4292-9c0c-fc412ae28f3f"
    }
}
```

**Example 2: 创建合同备注**



Input: 

```
tccli ess OperateFlowRemarks --cli-unfold-argument  \
    --Operator.UserId yDC**************************SXv \
    --OperateType CREATE \
    --FlowGroupId yD3**************************CkC \
    --FlowItems 合同组标签1
```

Output: 
```
{
    "Response": {
        "RequestId": "31b900d2-18ce-4304-9164-63fa98b6375e"
    }
}
```

