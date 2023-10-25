**Example 1: 创建三个合同组成的合同组**

1. 入参中FlowFileInfos有三个元素, 表示三个合同组成此合同组
2. 每个合同都是B2C合同

Input: 

```
tccli essbasic ChannelCreateFlowGroupByFiles --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId kevin \
    --Agent.ProxyOrganizationOpenId zk_online_org \
    --Agent.AppId 394fc83e7a1cc97ba27c3342f425c836 \
    --FlowGroupName 采购合同 \
    --FlowFileInfos.0.FileIds yDR1nUU06b46rUy0fKyKocxqVM6QwE88 \
    --FlowFileInfos.0.FlowName 番茄的采购合同 \
    --FlowFileInfos.0.Deadline 0 \
    --FlowFileInfos.0.FlowDescription 2023年番茄的采购50吨合同 \
    --FlowFileInfos.0.FlowType 采购合同 \
    --FlowFileInfos.0.CallbackUrl  \
    --FlowFileInfos.0.FlowApprovers.0.ApproverType ENTERPRISESERVER \
    --FlowFileInfos.0.FlowApprovers.0.OrganizationName 王五示例企业 \
    --FlowFileInfos.0.FlowApprovers.0.OrganizationOpenId zk_online_org \
    --FlowFileInfos.0.FlowApprovers.0.OpenId zk \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentRequired True \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentPosX 100 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentPosY 100 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowFileInfos.0.FlowApprovers.0.SignComponents.0.ComponentValue yDR1kUU0zproxUy0fKyKg4XBzdcXcTBg \
    --FlowFileInfos.0.FlowApprovers.1.Name 典子谦 \
    --FlowFileInfos.0.FlowApprovers.1.ApproverType PERSON \
    --FlowFileInfos.0.FlowApprovers.1.Mobile 13200000000 \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentRequired True \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentPosX 100 \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentPosY 200 \
    --FlowFileInfos.0.FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FlowFileInfos.0.CustomerData 5ZCI5ZCM5Lus5ZCI5ZCM5Lus \
    --FlowFileInfos.0.Unordered True \
    --FlowFileInfos.0.NeedSignReview False \
    --FlowFileInfos.1.FileIds yDR1nUU06b46rUy0fKyKocxqVM6QwE88 \
    --FlowFileInfos.1.FlowName 黄瓜的采购合同 \
    --FlowFileInfos.1.Deadline 0 \
    --FlowFileInfos.1.FlowDescription 2023年黄瓜的采购50吨合同 \
    --FlowFileInfos.1.FlowType 采购合同 \
    --FlowFileInfos.1.CallbackUrl  \
    --FlowFileInfos.1.FlowApprovers.0.ApproverType ENTERPRISESERVER \
    --FlowFileInfos.1.FlowApprovers.0.OrganizationName 李四示例企业 \
    --FlowFileInfos.1.FlowApprovers.0.OrganizationOpenId zk_online_org \
    --FlowFileInfos.1.FlowApprovers.0.OpenId zk \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentRequired True \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentPosX 100 \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentPosY 100 \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowFileInfos.1.FlowApprovers.0.SignComponents.0.ComponentValue yDR1kUU0zproxUy0fKyKg4XBzdcXcTBg \
    --FlowFileInfos.1.FlowApprovers.1.Name 典子谦 \
    --FlowFileInfos.1.FlowApprovers.1.ApproverType PERSON \
    --FlowFileInfos.1.FlowApprovers.1.Mobile 13200000000 \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentRequired True \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentPosX 100 \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentPosY 200 \
    --FlowFileInfos.1.FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FlowFileInfos.1.CustomerData 5paw55qE5a2Q5ZCI5ZCMMg== \
    --FlowFileInfos.1.Unordered True \
    --FlowFileInfos.1.NeedSignReview False \
    --FlowFileInfos.2.FileIds yDR1nUU06b46rUy0fKyKocxqVM6QwE88 \
    --FlowFileInfos.2.FlowName 马铃薯的采购合同 \
    --FlowFileInfos.2.Deadline 0 \
    --FlowFileInfos.2.FlowDescription 2023年马铃薯的采购50吨合同 \
    --FlowFileInfos.2.FlowType 采购合同 \
    --FlowFileInfos.2.CallbackUrl  \
    --FlowFileInfos.2.FlowApprovers.0.ApproverType ENTERPRISESERVER \
    --FlowFileInfos.2.FlowApprovers.0.OrganizationName 张三示例企业 \
    --FlowFileInfos.2.FlowApprovers.0.OrganizationOpenId zk_online_org \
    --FlowFileInfos.2.FlowApprovers.0.OpenId zk \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentRequired True \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentPosX 100 \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentPosY 100 \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowFileInfos.2.FlowApprovers.0.SignComponents.0.ComponentValue yDR1kUU0zproxUy0fKyKg4XBzdcXcTBg \
    --FlowFileInfos.2.FlowApprovers.1.Name 典子谦 \
    --FlowFileInfos.2.FlowApprovers.1.ApproverType PERSON \
    --FlowFileInfos.2.FlowApprovers.1.Mobile 13200000000 \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentRequired True \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentPosX 100 \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentPosY 200 \
    --FlowFileInfos.2.FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FlowFileInfos.2.CustomerData 5paw55qE5a2Q5ZCI5ZCMMw== \
    --FlowFileInfos.2.Unordered True \
    --FlowFileInfos.2.NeedSignReview False
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDwiSUUg0e3wmkUyoVjXzyZbNlhaVk85",
        "FlowIds": [
            "yDwiSUUg0e3wm2UyoVjXz1xWSYus0Jtc",
            "yDwiSUUg0e3wmrUyoVjXzSP9OEVRSAlk",
            "yDwiSUUg0e3wmhUyoVjXzByicWYPOymz"
        ],
        "RequestId": "s1698139089675399175"
    }
}
```

