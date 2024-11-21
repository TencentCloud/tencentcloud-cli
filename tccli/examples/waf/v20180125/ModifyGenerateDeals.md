**Example 1: 计费下单接口**



Input: 

```
tccli waf ModifyGenerateDeals --cli-unfold-argument  \
    --Goods.0.GoodsCategoryId 101201 \
    --Goods.0.GoodsNum 1 \
    --Goods.0.ProjectId 0 \
    --Goods.0.GoodsDetail.ProductCode p_wsm_waf \
    --Goods.0.GoodsDetail.LabelCounts 1 \
    --Goods.0.GoodsDetail.SubProductCode sp_wsm_waf_premium_clb \
    --Goods.0.GoodsDetail.TimeSpan 1 \
    --Goods.0.GoodsDetail.Type sp_wsm_waf_premium_clb \
    --Goods.0.GoodsDetail.RealRegion 0 \
    --Goods.0.GoodsDetail.ElasticQps 0 \
    --Goods.0.GoodsDetail.Pid 0 \
    --Goods.0.GoodsDetail.ProductInfo.0.Name 高级版 \
    --Goods.0.GoodsDetail.ProductInfo.0.Value 一套 \
    --Goods.0.GoodsDetail.AutoRenewFlag 1 \
    --Goods.0.GoodsDetail.FlexBill 0 \
    --Goods.0.GoodsDetail.TimeUnit m \
    --Goods.0.GoodsDetail.InstanceName guangzhoucase \
    --Goods.0.GoodsDetail.LabelTypes sv_wsm_waf_package_ultimate_clb \
    --Goods.0.RegionId 1 \
    --Goods.0.PayMode 1 \
    --Goods.0.Platform 0
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "Data": {
            "DealNames": [
                "20211127383000722205671"
            ],
            "BigDealId": "20211127383000722205661"
        },
        "ReturnMessage": "success",
        "RequestId": "b705af50-606d-46a7-8cb6-617f7592ed4e"
    }
}
```

