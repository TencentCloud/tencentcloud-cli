**Example 1: 文件发起**



Input: 

```
tccli ess CreateMiniAppPrepareFlow --cli-unfold-argument  \
    --Operator.UserId yDxjOUUgydjfxgnzUuO5zjEWA07rC5xl \
    --ResourceId yDtIfUUckp9grxnsUyecoDMwRdhpe8IE \
    --UserFlowTypeId  \
    --ResourceType 2 \
    --FlowName 小程序合同发起测试 \
    --Unordered True \
    --DeadlineAfterStartDays 3 \
    --UserData VXNlckRhdGE= \
    --FlowOption.NeedCreateReview False \
    --FlowOption.FlowDisplayType 1 \
    --PageOption.HideSignCodeAfterStart True \
    --CcInfos.0.CcType 0 \
    --CcInfos.0.Name 程某 \
    --CcInfos.0.Mobile 18700000000 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 电子签测试企业 \
    --Approvers.0.ApproverName 何规 \
    --Approvers.0.ApproverMobile 18200000000 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.ApproverName 张某 \
    --Approvers.1.ApproverMobile 18200000000
```

Output: 
```
{
    "Response": {
        "ExpiredOn": 1761031031,
        "FlowId": "yDtGEUUckp95buvoUuQn9oeynYWruYTL",
        "LongUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=CREATE_CONTRACT&shortKey=yDtGEUqBRu0a9TF5sO50",
        "MiniAppPath": "pages/guide/index?to=CREATE_CONTRACT&shortKey=yDtGEUqBRu0a9TF5sO50",
        "WeixinQrcodeUrl": "https://res.ess.tencent.cn/mp-gate/develop/CREATE_CONTRACT?shortKey=yDtGEUqBE5oBLdr2d590",
        "QrcodeUrl": "https://dyn.test.ess.tencent.cn/imgs/qrcode_urls/create_contract/yDtGEUUckp95bu13UuQn9oe1FEBKizIN.png",
        "RequestId": "s1753255031857612403",
        "ShortUrl": "https://test.essurl.cn/t8c0UBN27z"
    }
}
```

