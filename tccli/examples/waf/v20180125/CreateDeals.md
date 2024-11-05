**Example 1: 样例**



Input: 

```
tccli waf CreateDeals --cli-unfold-argument  \
    --Goods.0.GoodsCategoryId 0 \
    --Goods.0.GoodsNum 0 \
    --Goods.0.GoodsDetail.TimeSpan 1 \
    --Goods.0.GoodsDetail.TimeUnit m \
    --Goods.0.GoodsDetail.SubProductCode sp_wsm_waf_ultimate \
    --Goods.0.GoodsDetail.Pid 0 \
    --Goods.0.GoodsDetail.InstanceName cd-Default \
    --Goods.0.GoodsDetail.AutoRenewFlag 0 \
    --Goods.0.GoodsDetail.RealRegion 0 \
    --Goods.0.GoodsDetail.LabelTypes sv_wsm_waf_package_ultimate \
    --Goods.0.GoodsDetail.LabelCounts 1 \
    --Goods.0.GoodsDetail.CurDeadline 2024-10-21 12:45:00 \
    --Goods.0.GoodsDetail.InstanceId waf_22piczm885bfd9x5 \
    --Goods.0.GoodsDetail.ResourceId waf_22piczm885bfd9x5 \
    --Goods.0.RegionId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "DealNames": [
                "20241029942071711427531"
            ],
            "BigDealId": "20241029942071711427531"
        },
        "Status": 0,
        "ReturnMessage": "ok",
        "RequestId": "d55b94a8-07bb-4326-b82f-e6678151afe0"
    }
}
```

