**Example 1: 获取批量撤销签署流程链接**

指定需要批量撤回三个签署流程Id，获取批量撤销链接
接口调用成功返回批量撤回合同的链接，通过链接跳转到电子签小程序完成批量撤回

Input: 

```
tccli ess CreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowIds yDwhIUUck********Ekio7sxsMq yDwhIUUckp*******UuaXC88Rgc yDwhIUUckp*******7sySp2O5D38
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=BATCH_REVOKE_FLOW&tokenId=yDwhIUU*****BtD1PuoS7&userId=yD******4zjEwqXwsIljA&expireOn=1690536359&login=1&verify=1",
        "FailMessages": [
            "",
            "",
            ""
        ],
        "RequestId": "s1690449958963022285",
        "UrlExpireOn": "2023-07-28 17:25:59"
    }
}
```

**Example 2: 获取批量撤销签署流程链接失败**

获取批量撤销签署流程链接失败

Input: 

```
tccli ess CreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowIds yDwhIUUck********Ekio7sxsMq yDwhIUUckp*******UuaXC88Rgc yDwhIUUckp*******7sySp2O5D39
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "",
        "FailMessages": [
            "合同流程Id:xxx,无法撤回，错误信息：非本企业发起的合同",
            "合同流程Id:xxx,无法撤回，错误信息：非本企业发起的合同",
            "合同流程Id:xxx,无法撤回，错误信息：非本企业发起的合同"
        ],
        "UrlExpireOn": "",
        "RequestId": "s1690449958963022285"
    }
}
```

**Example 3: 获取批量撤销签署流程链接部分成功**

获取批量撤销签署流程链接部分成功

Input: 

```
tccli ess CreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowIds yDwhIUUck********Ekio7sxsMq yDwhIUUckp*******UuaXC88Rgc yDwhIUUckp*******7sySp2O5D38
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=BATCH_REVOKE_FLOW&tokenId=yDwhIUU*****BtD1PuoS7&userId=yD******4zjEwqXwsIljA&expireOn=1690536359&login=1&verify=1",
        "FailMessages": [
            "合同流程Id:xxx,无法撤回，错误信息：非本企业发起的合同",
            "",
            ""
        ],
        "RequestId": "s1690449958963022285",
        "UrlExpireOn": "2023-07-28 17:25:59"
    }
}
```

