**Example 1: 获取商品信息**

修改超时时间

Input: 

```
tccli billing DescribeGoodsVoucherList --cli-unfold-argument  \
    --SubType deduct \
    --Goods.0.GoodsCategoryId 101444 \
    --Goods.0.Zone ap-guangzhou-1 \
    --Goods.0.GoodsNum 1 \
    --Goods.0.ProjectId 0 \
    --Goods.0.Region ap-guangzhou \
    --Goods.0.PayMode 1 \
    --Goods.0.GoodsDetail {"buyr":"test","productInfo":[{"name":"计费测试商品","value":"jfcs"}],"productCode":"p_trade_t_s","subProductCode":"sp_trade_t_s","pid":16994,"timeUnit":"m","timeSpan":1,"action":"purchase","succCheck":1,"succ":1,"queryFlowType":1,"region":1,"trade_t_s":1} \
    --Limit 100 \
    --MainType no_price \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AvailableCount": 0,
        "VoucherInfos": [
            {
                "OwnerUin": "abc",
                "VoucherName": "abc",
                "VoucherId": "abc",
                "PolicyId": "abc",
                "Amount": 0,
                "LeftAmount": 0,
                "Status": "abc",
                "BeginTime": "abc",
                "EndTime": "abc",
                "CreateTime": "abc",
                "BatchCreateTime": "abc",
                "PayMode": "abc",
                "ActivityId": "abc",
                "ActivityName": "abc",
                "CodeId": "abc",
                "Creator": "abc",
                "UsedAmount": 0,
                "PayScene": "abc",
                "CouponType": "abc",
                "ProductDefine": "abc",
                "MinPayTime": "abc",
                "MaxPayTime": "abc",
                "UseDeadLine": "abc",
                "Available": true,
                "BaseAmount": 0,
                "UnavailableReason": [
                    0
                ],
                "GoodsTypeInfo": "abc",
                "GoodsName": "abc",
                "Reusable": 0,
                "ExcludedProduct": "abc",
                "VoucherMainType": "abc",
                "VoucherSubType": "abc",
                "DiscountRate": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

