**Example 1: 下单样例**

下单样例

Input: 

```
tccli waf GenerateDealsAndPayNew --cli-unfold-argument  \
    --Goods.0.GoodsCategoryId 101201 \
    --Goods.0.GoodsNum 1 \
    --Goods.0.GoodsDetail.TimeSpan 1 \
    --Goods.0.GoodsDetail.TimeUnit m \
    --Goods.0.GoodsDetail.SubProductCode sp_wsm_waf_premium_clb \
    --Goods.0.GoodsDetail.Pid 0 \
    --Goods.0.GoodsDetail.InstanceName anquan \
    --Goods.0.GoodsDetail.AutoRenewFlag 1 \
    --Goods.0.GoodsDetail.RealRegion 1 \
    --Goods.0.GoodsDetail.LabelTypes sv_wsm_waf_package_premium_clb \
    --Goods.0.GoodsDetail.LabelCounts 1 \
    --Goods.0.GoodsDetail.CurDeadline 2024-07-14 14:24:26 \
    --Goods.0.GoodsDetail.InstanceId waf_22piczpx8beg7rht \
    --Goods.0.RegionId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DealNames": [
                "20211127383000722205671"
            ],
            "BigDealId": "20211127383000722205661"
        },
        "Status": 0,
        "ReturnMessage": "success",
        "InstanceId": "waf_22piczpx8beg7rht",
        "RequestId": "b705af50-606d-46a7-8cb6-617f7592ed4e"
    }
}
```

