**Example 1: 获取商品信息**



Input: 

```
tccli billing DescribeGoodsVoucherList --cli-unfold-argument  \
    --Limit 100 \
    --Offset 1 \
    --Goods.0.GoodsCategoryId 101444 \
    --Goods.0.Region ap-guangzhou \
    --Goods.0.Zone ap-guangzhou-1 \
    --Goods.0.GoodsNum 1 \
    --Goods.0.ProjectId 0 \
    --Goods.0.PayMode 1 \
    --Goods.0.GoodsDetail {"buyr":"test","productInfo":[{"name":"计费测试商品","value":"jfcs"}],"productCode":"p_trade_t_s","subProductCode":"sp_trade_t_s","pid":16994,"timeUnit":"m","timeSpan":1,"action":"purchase","succCheck":1,"succ":1,"queryFlowType":1,"region":1,"trade_t_s":1} \
    --MainType no_price \
    --SubType deduct
```

Output: 
```
{
    "Response": {
        "AvailableCount": 1,
        "TotalCount": 1,
        "RequestId": "xx",
        "VoucherInfos": [
            {
                "ProductDefine": "xx",
                "PayScene": "xx",
                "PolicyId": "xx",
                "EndTime": "xx",
                "Status": "xx",
                "GoodsTypeInfo": "xx",
                "CouponType": "xx",
                "BatchCreateTime": "xx",
                "MinPayTime": "xx",
                "Available": true,
                "MaxPayTime": "xx",
                "ActivityName": "xx",
                "BaseAmount": 0,
                "OwnerUin": "xx",
                "PayMode": "xx",
                "ActivityId": "xx",
                "CodeId": "xx",
                "UnavailableReason": [
                    0
                ],
                "UseDeadLine": "xx",
                "Creator": "xx",
                "VoucherName": "xx",
                "Amount": 0,
                "VoucherId": "xx",
                "BeginTime": "xx",
                "UsedAmount": 0,
                "ExcludedProduct": "xx",
                "CreateTime": "xx",
                "LeftAmount": 0
            }
        ]
    }
}
```

