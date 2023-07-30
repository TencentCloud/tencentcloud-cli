**Example 1: 根据签署流程id创建批量撤回url**

指定需要批量撤回的签署流程Id，获取批量撤销链接
客户指定需要撤回的签署流程Id，最多100个，超过100不处理；接口调用成功返回批量撤回合同的链接，通过链接跳转到电子签小程序完成批量撤回

Input: 

```
tccli essbasic ChannelCreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId 600***487 \
    --Agent.ProxyOperator.OpenId 7f3497f0****7b0ec \
    --Agent.AppId 130****4283 \
    --FlowIds yDwF*****Xhgx9shH
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=BATCH_REVOKE_FLOW&tokenId=yDwhCUUck*****dKO5TA&userId=yDxHTUUgydj9*****yrY850RBN&expireOn=1690030266&login=1&verify=1",
        "FailMessages": [
            ""
        ],
        "RequestId": "e906c2a4-cb12-4f33-891e-39352d4dee3d",
        "UrlExpireOn": "2023-07-22 20:51:06"
    }
}
```

