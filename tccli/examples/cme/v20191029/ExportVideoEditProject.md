**Example 1: 导出视频到云点播**

 

Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform 1000000009 \
    --ProjectId cmepid_eb94392053f840539229ed9 \
    --Definition 10 \
    --ExportDestination VOD \
    --VODExportInfo.Name 在线编辑视频 \
    --VODExportInfo.ClassId 10 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "TaskId": "125xxxxxxx-tfusion-19f876370688d7d08eb10d6e4ecd1cd9",
        "RequestId": "725d0791-97d7-4e4a-8740-e2128b98ddf0"
    }
}
```

**Example 2: 导出视频到云点播并发布到企鹅号**

 

Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 10 \
    --ProjectId cmepid_eb94392053f840539229ed9 \
    --ExportDestination VOD \
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
        "TaskId": "125xxxxxxx-tfusion-00f08kd8e6370688d7d08eb10d6e4ec9kdu73",
        "RequestId": "789d5d0791-97d7-4e4a-8740-e2128b98ddf0"
    }
}
```

**Example 3: 导出视频到多媒体创作引擎媒资库**

 

Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform 1000000009 \
    --ProjectId cmepid_eb94392053f840539229ed9 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "TaskId": "125xxxxxxx-tfusion-62f876370688d7d08eb10d6e4ecd1cd9",
        "RequestId": "233d0791-97d7-4e4a-8740-e2128b032df8"
    }
}
```

**Example 4: 导出视频到多媒体创作引擎媒资库并发布到企鹅号**

 

Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform 1000000009 \
    --Definition 10 \
    --ExportDestination CME \
    --ProjectId cmepid_eb94392053f840539229ed9 \
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
        "TaskId": "125xxxxxxx-tfusion-82f876370688d7d08eb10d6e4ecd1cd9",
        "RequestId": "733d0791-97d7-4e4a-8740-e2128b032df2"
    }
}
```

**Example 5: 导出视频多媒体创作引擎媒资库并指定导出视频的码率**

导出视频多媒体创作引擎媒资库并指定导出视频的码率为 3M bps

Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform 1000000009 \
    --ProjectId cmepid_eb94392053f840539229ed9 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0 \
    --ExportExtensionArgs.VideoBitrate 3145728 \
    --Operator 9b92a8e7-a5ef-4e28-d72e-4eff571fabf0
```

Output: 
```
{
    "Response": {
        "TaskId": "125xxxxxxx-tfusion-72f876370688d7d08eb10d6e4ecd1cd9",
        "RequestId": "533d0791-97d7-4e4a-8740-e2128b032df9"
    }
}
```

