**Example 1: 预释放出价**



Input: 

```
tccli domain BiddingPreRelease --cli-unfold-argument  \
    --BusinessId P0011702977661022561 \
    --Price 100.0
```

Output: 
```
{
    "Response": {
        "IsNeedPay": true,
        "BillingParam": ">{\"uin\":\"100*****091\",\"ownerUin\":\"100*****091\",\"appId\":10000,\"goods\":[{\"goodsCategoryId\":100,\"regionId\":47,\"zoneId\":470004,\"goodsNum\":1,\"projectId\":0,\"payMode\":1,\"goodsDetail\":{\"pid\":1000,\"productCode\":\"p_d\",\"subProductCode\":\"sp_d_*\",\"productInfo\":[{\"name\":\"预释放竞价保证金订单\",\"value\":\"竞价域名：att.com\"}],\"domain\":\"att.com\",\"timeSpan\":1,\"timeUnit\":\"p\",\"autoRenewFlag\":0,\"createType\":\"bid_deposit\",\"price\":10000,\"bondPrice\":0,\"biddingBondPrice\":100,\"sv_d\":1,\"businessId\":\"P0********945\",\"isAutoPay\":0,\"templateId\":\"\"}}]}",
        "RequestId": "dwde-f405-gg33-fee223"
    }
}
```

