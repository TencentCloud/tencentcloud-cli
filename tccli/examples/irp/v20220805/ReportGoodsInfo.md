**Example 1: 上报商品内容信息**

上报商品内容信息

Input: 

```
tccli irp ReportGoodsInfo --cli-unfold-argument  \
    --GoodsList.0.GoodsId 20220112A02JTB01 \
    --GoodsList.0.GoodsType article \
    --GoodsList.0.Status 1 \
    --GoodsList.0.PublishTimestamp 1641459038 \
    --GoodsList.0.ExpireTimestamp 1642668637 \
    --GoodsList.0.CategoryLevel 3 \
    --GoodsList.0.CategoryPath 数码产品:手机:华为 \
    --GoodsList.0.Tags 手机;翻盖 \
    --GoodsList.0.SourceId 1 \
    --GoodsList.0.Title 标题 \
    --GoodsList.0.Content 123 \
    --GoodsList.0.ContentUrl https://xx/xxx \
    --GoodsList.0.Country CN \
    --GoodsList.0.Province CN-GD \
    --GoodsList.0.City 440100 \
    --GoodsList.0.CollectCnt 11 \
    --GoodsList.0.PraiseCnt 11 \
    --GoodsList.0.CommentCnt 11 \
    --GoodsList.0.ShareCnt 11 \
    --GoodsList.0.Score 9.7 \
    --GoodsList.0.Extension {} \
    --InstanceId 3154571c_d511
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

