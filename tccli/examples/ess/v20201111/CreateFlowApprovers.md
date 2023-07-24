**Example 1: 补充签署流程本企业签署人信息**

补充签署流程本企业签署人信息



Input: 

```
tccli ess CreateFlowApprovers --cli-unfold-argument  \
    --Operator.UserId  \
    --FlowId flow_id_xxxxx \
    --Initiator xxx \
    --Approvers.0.RecipientId RecipientId_1 \
    --Approvers.0.ApproverSource WEWORKAPP \
    --Approvers.0.CustomUserId Zhangsan \
    --Approvers.1.RecipientId RecipientId_1 \
    --Approvers.1.ApproverSource WEWORKAPP \
    --Approvers.1.CustomUserId Lisi \
    --Approvers.2.RecipientId RecipientId_2 \
    --Approvers.2.ApproverSource WEWORKAPP \
    --Approvers.2.CustomUserId Wangwu \
    --Approvers.3.RecipientId RecipientId_2 \
    --Approvers.3.ApproverSource WEWORKAPP \
    --Approvers.3.CustomUserId ZhaoLiu \
    --Approvers.4.RecipientId RecipientId_3 \
    --Approvers.4.ApproverName 典子谦 \
    --Approvers.4.ApproverMobile 1820000xxxx \
    --Approvers.5.RecipientId RecipientId_3 \
    --Approvers.5.ApproverName 何规 \
    --Approvers.5.ApproverMobile 1830000xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "2846e98d-7f-d2632a7fceef"
    }
}
```

