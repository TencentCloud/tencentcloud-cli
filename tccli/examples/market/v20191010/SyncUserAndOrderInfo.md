**Example 1: 例子**



Input: 

```
tccli market SyncUserAndOrderInfo --cli-unfold-argument  \
    --UserInfo.PaidCorpName xx \
    --UserInfo.PaidCorpId xx \
    --OrderInfo.OrderId xx \
    --OrderInfo.OrderTime 0 \
    --OrderInfo.EditionName xx \
    --OrderInfo.OrderType 0 \
    --OrderInfo.Price 0 \
    --OrderInfo.EditionId xx \
    --OrderInfo.Remark xx \
    --OrderInfo.Deals.ProductCode xx \
    --OrderInfo.Deals.SubBillingItemCode xx \
    --OrderInfo.Deals.BillingItemCode xx \
    --OrderInfo.Deals.SubProductCode xx \
    --OrderInfo.Deals.TimeSpan 0.0 \
    --OrderInfo.Deals.Discount 0.0 \
    --OrderInfo.Deals.DosageUnit xx \
    --OrderInfo.Deals.Fee 0 \
    --OrderInfo.Deals.TimeUnit xx \
    --OrderInfo.Deals.OriginPrice 0 \
    --OrderInfo.Deals.UnitPrice 0.0 \
    --OrderInfo.Deals.Dosage 0.0 \
    --OrderInfo.SuiteId xx \
    --OrderInfo.OrderStatus 0 \
    --OrderInfo.UseEndTime 0 \
    --OrderInfo.UseBeginTime 0 \
    --OrderInfo.PaidTime 0
```

Output: 
```
{
    "Response": {
        "Info": {
            "Message": "xx",
            "Code": "xx"
        },
        "Details": {
            "TotalCount": 1,
            "OwnerUin": "xx",
            "MarketOrders": [
                "10001",
                "10002"
            ]
        },
        "RequestId": "xx"
    }
}
```

