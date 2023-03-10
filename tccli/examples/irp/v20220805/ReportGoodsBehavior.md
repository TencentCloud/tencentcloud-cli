**Example 1: 上报商品用户行为**



Input: 

```
tccli irp ReportGoodsBehavior --cli-unfold-argument  \
    --InstanceId dd77b984_d517 \
    --GoodsBehaviorList.0.UserId 3154571 \
    --GoodsBehaviorList.0.GoodsId 1232 \
    --GoodsBehaviorList.0.Page 首页 \
    --GoodsBehaviorList.0.Module 猜你喜欢 \
    --GoodsBehaviorList.0.BehaviorType expose \
    --GoodsBehaviorList.0.BehaviorValue 1 \
    --GoodsBehaviorList.0.BehaviorTimestamp 1652705901 \
    --GoodsBehaviorList.0.SceneId db5ccd_765291 \
    --GoodsBehaviorList.0.ReferrerGoodsId 1231 \
    --GoodsBehaviorList.0.Source tencent \
    --GoodsBehaviorList.0.Extension {}
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

