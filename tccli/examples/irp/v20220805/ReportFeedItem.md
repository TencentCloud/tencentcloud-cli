**Example 1: 上报信息流内容**



Input: 

```
tccli irp ReportFeedItem --cli-unfold-argument  \
    --FeedItemList.0.ItemId 20220112A02JTB01 \
    --FeedItemList.0.ItemType article \
    --FeedItemList.0.Status 1 \
    --FeedItemList.0.PublishTimestamp 1641459038 \
    --FeedItemList.0.ExpireTimestamp 1642668637 \
    --FeedItemList.0.CategoryLevel 3 \
    --FeedItemList.0.CategoryPath 体育:足球:巴塞罗纳 \
    --FeedItemList.0.Tags 体育:娱乐 \
    --FeedItemList.0.Author 作者名 \
    --FeedItemList.0.SourceId 1 \
    --FeedItemList.0.Title 标题 \
    --FeedItemList.0.Content 杜兰特又夺冠，篮网银河巨舰 \
    --FeedItemList.0.ContentUrl https://xx/xxx \
    --FeedItemList.0.VideoDuration 60 \
    --FeedItemList.0.Country CN \
    --FeedItemList.0.Province CN-GD \
    --FeedItemList.0.City 440100 \
    --FeedItemList.0.AuthorFans 1 \
    --FeedItemList.0.AuthorLevel 高级 \
    --FeedItemList.0.CollectCnt 11 \
    --FeedItemList.0.PraiseCnt 11 \
    --FeedItemList.0.CommentCnt 11 \
    --FeedItemList.0.ShareCnt 11 \
    --FeedItemList.0.RewardCnt 11 \
    --FeedItemList.0.Score 9.7 \
    --FeedItemList.0.Extension {} \
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

