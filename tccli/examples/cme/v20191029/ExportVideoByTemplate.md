**Example 1: 使用模板导出视频到云点播**



Input: 

```
tccli cme ExportVideoByTemplate --cli-unfold-argument  \
    --Platform test \
    --TemplateId 60498a50adaf8f000164a07b@prod@12500000 \
    --SlotReplacements.0.Id 1 \
    --SlotReplacements.0.ReplacementType VIDEO \
    --SlotReplacements.0.MediaReplacementInfo.MaterialId 5fc4ad7f69ec74000179072345 \
    --SlotReplacements.0.MediaReplacementInfo.StartTimeOffset 0 \
    --Definition 10 \
    --ExportDestination VOD \
    --VODExportInfo.Name 测试视频 \
    --VODExportInfo.ClassId 10000
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

**Example 2: 使用模板导出视频到剪媒资**



Input: 

```
tccli cme ExportVideoByTemplate --cli-unfold-argument  \
    --Platform test \
    --TemplateId 60498a50adaf8f000164a07b@prod@12500000 \
    --SlotReplacements.0.Id 1 \
    --SlotReplacements.0.ReplacementType VIDEO \
    --SlotReplacements.0.MediaReplacementInfo.MaterialId 5fc4ad7f69ec74000179072345 \
    --SlotReplacements.0.MediaReplacementInfo.StartTimeOffset 0 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSION \
    --CMEExportInfo.Owner.Id 119993993939390 \
    --CMEExportInfo.Name 测试视频 \
    --CMEExportInfo.ClassPath /素材/视频
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

