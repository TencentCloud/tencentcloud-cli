**Example 1: 上报信息流行为**



Input: 

```
tccli irp ReportFeedBehavior --cli-unfold-argument  \
    --InstanceId dd77b984_d517 \
    --FeedBehaviorList.0.UserId 3154571 \
    --FeedBehaviorList.0.ItemId 1232 \
    --FeedBehaviorList.0.BehaviorType expose \
    --FeedBehaviorList.0.BehaviorValue 1 \
    --FeedBehaviorList.0.BehaviorTimestamp 1652705901 \
    --FeedBehaviorList.0.SceneId db5ccd_765291 \
    --FeedBehaviorList.0.ItemTraceId 9994f7bc21231288365e0f773 \
    --FeedBehaviorList.0.ItemType article \
    --FeedBehaviorList.0.ReferrerItemId 1231 \
    --FeedBehaviorList.0.UserIdList.0.Type qq \
    --FeedBehaviorList.0.UserIdList.0.Value 313211 \
    --FeedBehaviorList.0.UserIdList.1.Type imei_md5 \
    --FeedBehaviorList.0.UserIdList.1.Value 9994f7bc21231288365e0f773dc81cec186 \
    --FeedBehaviorList.0.Source tencent \
    --FeedBehaviorList.0.Country CN \
    --FeedBehaviorList.0.Province CN-GD \
    --FeedBehaviorList.0.City 440100 \
    --FeedBehaviorList.0.IP 127.0.0.1 \
    --FeedBehaviorList.0.Network wifi \
    --FeedBehaviorList.0.Platform android \
    --FeedBehaviorList.0.AppVersion 11 \
    --FeedBehaviorList.0.OsVersion 7.2 \
    --FeedBehaviorList.0.DeviceModel xiaomi \
    --FeedBehaviorList.0.Extension {}
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

