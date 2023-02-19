**Example 1: 使用视频编辑轨道数据导出视频到云点播**

使用视频编辑轨道数据导出视频到云点播，并指定操作者。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform default_platform \
    --Definition 10 \
    --ExportDestination VOD \
    --TrackData track_data_xxxx \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --Operator user_id_9394392053f8405394299d8
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
    --Platform test \
    --AspectRatio 16:9 \
    --TrackData track_data_xxxx \
    --Definition 10 \
    --ExportDestination VOD \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --Operator user_id_9394392053f8405394299d8
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
    --Platform test \
    --AspectRatio 16:9 \
    --TrackData track_data_xxxx \
    --Definition 10 \
    --ExportDestination VOD \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --VODExportInfo.ThirdPartyPublishInfos.0.ChannelMaterialId 5fd8ad3d628dc30001bd0895 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Title 企鹅视频 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Description 新闻 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Tags 娱乐 \
    --VODExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Category 100 \
    --Operator user_id_9394392053f8405394299d8
```

Output: 
```
{
    "Response": {
        "RequestId": "e86c730b-97c8-4e7d-b4a1-f5b28291e2b3",
        "TaskId": "181xxxxxx01-FusionCME-c85bf7f3b9b4c594fbd558800a6fecb7t"
    }
}
```

**Example 4: 使用视频编辑轨道数据导出视频到多媒体创作引擎媒资库**

使用视频编辑轨道数据导出视频到多媒体创作引擎媒资库。

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform test \
    --AspectRatio 16:9 \
    --TrackData track_data_xxx \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id ed3fa411-73e6-4fd0-abe2-498bf5f9e7f0 \
    --CMEExportInfo.Name 新建项目 \
    --CMEExportInfo.ClassPath /成片
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
    --Platform test \
    --AspectRatio 16:9 \
    --TrackData track_data_xxxx \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id ed3fa411-73e6-4fd0-abe2-498bf5f9e7f0 \
    --CMEExportInfo.Name 新建项目 \
    --CMEExportInfo.ClassPath /成片 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.ChannelMaterialId 5fd8ad3d628dc30001bd0895 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Title 企鹅视频 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Description 新闻 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Tags 娱乐 \
    --CMEExportInfo.ThirdPartyPublishInfos.0.PenguinMediaPlatformPublishInfo.Category 100 \
    --Operator user_id_9394392053f8405394299d8
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

