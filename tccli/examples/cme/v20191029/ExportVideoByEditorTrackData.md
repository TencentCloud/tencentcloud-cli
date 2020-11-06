**Example 1: 使用视频编辑轨道数据导出视频**



Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform default_platform \
    --Definition 10 \
    --ExportDestination VOD \
    --TrackData [] \
    --VODExportInfo.Name 在线编辑视频 \
    --Operator 16556266637489
```

Output: 
```
{
    "Response": {
        "TaskId": "125009388839-tfusion-0a54392053f84053942f9308c49404d7",
        "RequestId": "0a543920-53f8-4053-942f-9308c49404d7"
    }
}
```

