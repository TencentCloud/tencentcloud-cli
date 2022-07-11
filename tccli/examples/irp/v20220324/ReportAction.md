**Example 1: 上报行为数据**



Input: 

```
tccli irp ReportAction --cli-unfold-argument  \
    --Bid dd77b984_d517 \
    --DocBehaviorList.0.ItemType 1 \
    --DocBehaviorList.0.IP 127.0.0.1 \
    --DocBehaviorList.0.BehaviorType 1 \
    --DocBehaviorList.0.Platform android \
    --DocBehaviorList.0.City 深圳 \
    --DocBehaviorList.0.RecTraceId abab \
    --DocBehaviorList.0.Network wifi \
    --DocBehaviorList.0.District 南山 \
    --DocBehaviorList.0.BehaviorTimestamp 1652705901 \
    --DocBehaviorList.0.AppVersion 11 \
    --DocBehaviorList.0.Source tencent \
    --DocBehaviorList.0.UserIdList.0.UserIdType 1 \
    --DocBehaviorList.0.UserIdList.0.UserId 313211 \
    --DocBehaviorList.0.UserIdList.1.UserIdType 4 \
    --DocBehaviorList.0.UserIdList.1.UserId 9994f7bc21231288365e0f773dc81cec186 \
    --DocBehaviorList.0.ReferrerItemId 1231 \
    --DocBehaviorList.0.Province 广东 \
    --DocBehaviorList.0.SceneId db5ccd_765291 \
    --DocBehaviorList.0.AppId wxe0135baa2b2554e8 \
    --DocBehaviorList.0.OsVersion 7.2 \
    --DocBehaviorList.0.BehaviorValue 1 \
    --DocBehaviorList.0.ItemId 1232 \
    --DocBehaviorList.0.DeviceModel xiaomi \
    --DocBehaviorList.0.Extension {} \
    --DocBehaviorList.0.Country CN \
    --DocBehaviorList.0.VideoPlayDuration 100
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

