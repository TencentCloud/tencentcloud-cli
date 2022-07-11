**Example 1: 上报推荐物料**



Input: 

```
tccli irp ReportMaterial --cli-unfold-argument  \
    --DocItemList.0.Status 1 \
    --DocItemList.0.Province 广东 \
    --DocItemList.0.PublishTimestamp 1641459038 \
    --DocItemList.0.ItemType 1 \
    --DocItemList.0.City 深圳 \
    --DocItemList.0.ExpireTimestamp 1642668637 \
    --DocItemList.0.AuthorLevel 高级 \
    --DocItemList.0.TagInfoList.0.Id 921 \
    --DocItemList.0.TagInfoList.0.Name abcd \
    --DocItemList.0.TagInfoList.0.Weight 9.7 \
    --DocItemList.0.TagInfoList.1.Id 1232 \
    --DocItemList.0.TagInfoList.1.Name tag1232 \
    --DocItemList.0.TagInfoList.1.Weight 123.32 \
    --DocItemList.0.PicUrlList https://sm.ms/image/IbHa5MkJivPxLNj https://sm.ms/image/IbHa5MkJivPxLNj \
    --DocItemList.0.ShareCnt 11 \
    --DocItemList.0.Topic 体育 \
    --DocItemList.0.AuthorId 作者id \
    --DocItemList.0.CollectCnt 11 \
    --DocItemList.0.VideoUrlList https://sm.ms/image/IbHa5MkJivPxLNj https://sm.ms/image/IbHa5MkJivPxLNj \
    --DocItemList.0.CategoryPath 体育:足球:巴塞罗纳 \
    --DocItemList.0.Desc 杜兰特又夺冠，篮网银河巨舰 \
    --DocItemList.0.ItemId 20220112A02JTB01 \
    --DocItemList.0.VideoDuration 60 \
    --DocItemList.0.PoolIdList 123 211 1221 \
    --DocItemList.0.District 南山 \
    --DocItemList.0.Keyword 体育、篮球 \
    --DocItemList.0.Title 标题 \
    --DocItemList.0.SourceId 1 \
    --DocItemList.0.Country CN \
    --DocItemList.0.Author 作者 \
    --DocItemList.0.Content 杜兰特又夺冠，篮网银河巨舰 \
    --DocItemList.0.Extension {} \
    --DocItemList.0.Score 9.7 \
    --DocItemList.0.AuthorFans 1 \
    --DocItemList.0.CategoryLevel 3 \
    --DocItemList.0.PraiseCnt 11 \
    --DocItemList.0.CommentCnt 11 \
    --DocItemList.0.RewardCnt 11 \
    --Bid 3154571c_d511
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

