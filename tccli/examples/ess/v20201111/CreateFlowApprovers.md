**Example 1: 测试**



Input: 

```
tccli ess CreateFlowApprovers --cli-unfold-argument  \
    --Operator.UserId  \
    --FlowId flow_id_xxxxx \
    --Initiator xxx \
    --Approvers.0.RecipientId RecipientId_1 \
    --Approvers.0.ApproverSource WEWORK \
    --Approvers.0.CustomUserId Zhangsan \
    --Approvers.1.RecipientId RecipientId_1 \
    --Approvers.1.ApproverSource WEWORK \
    --Approvers.1.CustomUserId Lisi \
    --Approvers.2.RecipientId RecipientId_2 \
    --Approvers.2.ApproverSource WEWORK \
    --Approvers.2.CustomUserId Wangwu \
    --Approvers.3.RecipientId RecipientId_2 \
    --Approvers.3.ApproverSource WEWORK \
    --Approvers.3.CustomUserId ZhaoLiu
```

Output: 
```
{
    "Response": {
        "RequestId": "2846e98d-7f-d2632a7fceef"
    }
}
```

