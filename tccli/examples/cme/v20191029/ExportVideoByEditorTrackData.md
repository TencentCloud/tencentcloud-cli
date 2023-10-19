**Example 1: 使用视频编辑轨道数据导出视频到云点播**

使用视频编辑轨道数据导出视频到云点播，并指定操作者。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 10 \
    --ExportDestination VOD \
    --TrackData {"id":"baa03b1c-6773-4459-a7b3-7f1e8b9e5b56","type":"video","items":[{"id":"f244311c-ca04-447a-b49a-1226356d46ba","start_time":0,"duration":3000,"type":"image","asset_id":"6503fd9d17509729a6100011","filter_asset_id":"","operations":[{"type":"image_rotate","params":{"angle":0}}],"width":540,"height":540,"position":{"x":480,"y":300},"section":{"from":0,"to":3000}}]} \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --ExportExtensionArgs.FrameRate 30 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "TaskId": "1250093889-tfusion-0a54392053f84053942f9308c49404d7",
        "RequestId": "0a543920-53f8-4053-942f-9308c49404d7"
    }
}
```

**Example 2: 使用视频编辑轨道数据导出视频到云点播并指定导出视频宽高比**

使用视频编辑轨道数据导出视频到云点播，同时指定导出视频宽高比且指定操作者。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 10 \
    --ExportDestination VOD \
    --AspectRatio 16:9 \
    --TrackData {"id":"baa03b1c-6773-4459-a7b3-7f1e8b9e5b56","type":"video","items":[{"id":"f244311c-ca04-447a-b49a-1226356d46ba","start_time":0,"duration":3000,"type":"image","asset_id":"6503fd9d17509729a6100011","filter_asset_id":"","operations":[{"type":"image_rotate","params":{"angle":0}}],"width":540,"height":540,"position":{"x":480,"y":300},"section":{"from":0,"to":3000}}]} \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "TaskId": "181xxxxxx01-FusionCME-c85bf7f3b9b4c594fbd558800a6fecb5t",
        "RequestId": "e86c730b-97c8-4e7d-b4a1-f5b28291e2b3"
    }
}
```

**Example 3: 使用视频编辑轨道数据导出视频到云点播并发布到企鹅号**

使用视频编辑轨道数据导出视频到云点播，并将导出的视频发布到企鹅号。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 10 \
    --ExportDestination VOD \
    --TrackData {"id":"baa03b1c-6773-4459-a7b3-7f1e8b9e5b56","type":"video","items":[{"id":"f244311c-ca04-447a-b49a-1226356d46ba","start_time":0,"duration":3000,"type":"image","asset_id":"6503fd9d17509729a6100011","filter_asset_id":"","operations":[{"type":"image_rotate","params":{"angle":0}}],"width":540,"height":540,"position":{"x":480,"y":300},"section":{"from":0,"to":3000}}]} \
    --AspectRatio 16:9 \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --VODExportInfo.ThirdPartyPublishInfos.0.ChannelMaterialId 5fd8ad3d628dc30001bd0895 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Title 企鹅视频 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Description 新闻 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Tags 娱乐 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Category 100 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "TaskId": "e86c730b-97c8-4e7d-b4a1-f5b28291e2b3",
        "RequestId": "181xxxxxx01-FusionCME-c85bf7f3b9b4c594fbd558800a6fecb7t"
    }
}
```

**Example 4: 使用视频编辑轨道数据导出视频到多媒体创作引擎媒资库**

使用视频编辑轨道数据导出视频到多媒体创作引擎媒资库。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 1 \
    --ExportDestination CME \
    --AspectRatio 16:9 \
    --TrackData {"id":"baa03b1c-6773-4459-a7b3-7f1e8b9e5b56","type":"video","items":[{"id":"f244311c-ca04-447a-b49a-1226356d46ba","start_time":0,"duration":3000,"type":"image","asset_id":"6503fd9d17509729a6100011","filter_asset_id":"","operations":[{"type":"image_rotate","params":{"angle":0}}],"width":540,"height":540,"position":{"x":480,"y":300},"section":{"from":0,"to":3000}}]} \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0 \
    --CMEExportInfo.Name 新建项目 \
    --CMEExportInfo.ClassPath /成片 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "RequestId": "e86c730b-97c8-4e7d-b4a1-f5b28291e2b3",
        "TaskId": "181xxxxxx01-FusionCME-c85bf7f3b9b4c594fbd558800a6fecb5t"
    }
}
```

**Example 5: 使用视频编辑轨道数据导出视频到多媒体创作引擎媒资库并发布到企鹅号**

使用视频编辑轨道数据导出视频到多媒体创作引擎媒资库并发布到企鹅号。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 1 \
    --ExportDestination CME \
    --AspectRatio 16:9 \
    --TrackData {"id":"baa03b1c-6773-4459-a7b3-7f1e8b9e5b56","type":"video","items":[{"id":"f244311c-ca04-447a-b49a-1226356d46ba","start_time":0,"duration":3000,"type":"image","asset_id":"6503fd9d17509729a6100011","filter_asset_id":"","operations":[{"type":"image_rotate","params":{"angle":0}}],"width":540,"height":540,"position":{"x":480,"y":300},"section":{"from":0,"to":3000}}]} \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0 \
    --CMEExportInfo.Name 新建项目 \
    --CMEExportInfo.ClassPath /成片 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.ChannelMaterialId 5fd8ad3d628dc30001bd0895 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Title 企鹅视频 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Description 新闻 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Tags 娱乐 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Category 100 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "RequestId": "e86c730b-97c8-4e7d-b4a1-f5b28291e2b3",
        "TaskId": "181xxxxxx01-FusionCME-c82bf7f3b9b4c594fbd558800a6fe7c5t"
    }
}
```

