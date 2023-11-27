**Example 1: 下单样例**

下单样例

Input: 

```
tccli waf GenerateDealsAndPayNew --cli-unfold-argument  \
    --Goods.0.GoodsCategoryId 0 \
    --Goods.0.GoodsNum 0 \
    --Goods.0.GoodsDetail.TimeSpan 0 \
    --Goods.0.GoodsDetail.TimeUnit abc \
    --Goods.0.GoodsDetail.SubProductCode abc \
    --Goods.0.GoodsDetail.Pid 0 \
    --Goods.0.GoodsDetail.InstanceName abc \
    --Goods.0.GoodsDetail.AutoRenewFlag 0 \
    --Goods.0.GoodsDetail.RealRegion 0 \
    --Goods.0.GoodsDetail.LabelTypes abc \
    --Goods.0.GoodsDetail.LabelCounts 0 \
    --Goods.0.GoodsDetail.CurDeadline abc \
    --Goods.0.GoodsDetail.InstanceId abc \
    --Goods.0.RegionId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "DealNames": [
                "abc"
            ],
            "BigDealId": "abc"
        },
        "Status": 0,
        "ReturnMessage": "abc",
        "InstanceId": "abc",
        "RequestId": "abc"
    }
}
```

