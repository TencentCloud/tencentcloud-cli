**Example 1: 使用剪辑模板导出视频到云点播**

 

Input: 

```
tccli cme ExportVideoByTemplate --cli-unfold-argument  \
    --Platform test \
    --TemplateId 60498a50adaf8f000164a07b@prod@12500000 \
    --SlotReplacements.0.Id 1 \
    --SlotReplacements.0.ReplacementType VIDEO \
    --SlotReplacements.0.MediaReplacementInfo.MediaType CMEMaterialId \
    --SlotReplacements.0.MediaReplacementInfo.MaterialId 5fc4ad7f69ec74000179072345 \
    --SlotReplacements.0.MediaReplacementInfo.StartTimeOffset 0 \
    --Definition 10 \
    --ExportDestination VOD \
    --VODExportInfo.Name 测试视频 \
    --VODExportInfo.ClassId 10000 \
    --Operator user_id_9394392053f8405394299d8
```

Output: 
```
{
    "Response": {
        "TaskId": "1250000000-tfusion-32f87637061242508eb10d6e4ecd0cd6",
        "RequestId": "0b480791-97d7-4e4a-8740-e2128b871df6"
    }
}
```

**Example 2: 使用剪辑模板导出视频到多媒体创作引擎媒资**

 

Input: 

```
tccli cme ExportVideoByTemplate --cli-unfold-argument  \
    --Platform 123000111 \
    --TemplateId 60498a50adaf8f000164a07b@prod@12500000 \
    --SlotReplacements.0.Id 1 \
    --SlotReplacements.0.ReplacementType IMAGE \
    --SlotReplacements.0.MediaReplacementInfo.MediaType CMEMaterialId \
    --SlotReplacements.0.MediaReplacementInfo.MaterialId becff2c5e7d77a9e0353 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id 1a69f09d-1a28-4437-a71a \
    --CMEExportInfo.Name 模版测试1009 \
    --CMEExportInfo.ClassPath /媒资 \
    --ExportExtensionArgs.VideoBitrate 102400 \
    --ExportExtensionArgs.FrameRate 30 \
    --Operator user_id_9394392053f8405394299d8
```

Output: 
```
{
    "Response": {
        "TaskId": "1250000000-tfusion-32f87637061242508eb10d6e4ecd0cd7",
        "RequestId": "323d0791-97d7-4e4a-8740-e2128b031df7"
    }
}
```

**Example 3: 使用剪辑模板导出视频到云点播并发布到企鹅号**

 

Input: 

```
tccli cme ExportVideoByTemplate --cli-unfold-argument  \
    --Platform test \
    --TemplateId 60498a50adaf8f000164a07b@prod@12500000 \
    --SlotReplacements.0.Id 1 \
    --SlotReplacements.0.ReplacementType VIDEO \
    --SlotReplacements.0.MediaReplacementInfo.MediaType CMEMaterialId \
    --SlotReplacements.0.MediaReplacementInfo.MaterialId 5fc4ad7f69ec74000179072345 \
    --SlotReplacements.0.MediaReplacementInfo.StartTimeOffset 0 \
    --Definition 10 \
    --ExportDestination VOD \
    --VODExportInfo.Name 测试视频 \
    --VODExportInfo.ClassId 10000 \
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
        "TaskId": "1250000000-tfusion-32f87637061242508eb10d6e4ecd0cd8",
        "RequestId": "323d0791-97d7-4e4a-8740-e2128b031df8"
    }
}
```

**Example 4: 使用剪辑模板导出视频到多媒体创作引擎媒资并发布到企鹅号**

 

Input: 

```
tccli cme ExportVideoByTemplate --cli-unfold-argument  \
    --Platform test \
    --TemplateId 60498a50adaf8f000164a07b@prod@12500000 \
    --SlotReplacements.0.Id 1 \
    --SlotReplacements.0.ReplacementType VIDEO \
    --SlotReplacements.0.MediaReplacementInfo.MediaType CMEMaterialId \
    --SlotReplacements.0.MediaReplacementInfo.MaterialId 5fc4ad7f69ec74000179072345 \
    --SlotReplacements.0.MediaReplacementInfo.StartTimeOffset 0 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSION \
    --CMEExportInfo.Owner.Id 119993993939390 \
    --CMEExportInfo.Name 测试视频 \
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
        "TaskId": "1250000000-tfusion-32f87637061242508eb10d6e4ecd0cd8",
        "RequestId": "89dle791-97d7-4e4a-8740-e2128b038ad9"
    }
}
```

