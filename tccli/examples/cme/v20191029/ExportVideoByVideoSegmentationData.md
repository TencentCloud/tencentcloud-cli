**Example 1: 使用视频智能拆条数据导出视频到CME**



Input: 

```
tccli cme ExportVideoByVideoSegmentationData --cli-unfold-argument  \
    --Definition 10 \
    --ProjectId cmepid_5fd1dfaf0e1b530001f5d9b0 \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id 08f06c7c1fdddbea083f899b932c4987 \
    --CMEExportInfo.ClassPath /媒资/视频 \
    --CMEExportInfo.Name 在线编辑视频 \
    --ExportDestination CME \
    --Platform default_platform \
    --Operator 16556266637489 \
    --SegmentGroupId 5fd6e20b0e1b530001f5daed \
    --SegmentIds seg_5fd6e2100e1b530001f5daef seg_5fd6e20b0e1b530001f5daee
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

**Example 2: 使用视频智能拆条数据导出视频到VOD**



Input: 

```
tccli cme ExportVideoByVideoSegmentationData --cli-unfold-argument  \
    --Definition 10 \
    --ProjectId cmepid_5fd1dfaf0e1b530001f5d9b0 \
    --ExportDestination VOD \
    --Platform default_platform \
    --VODExportInfo.Name 在线编辑视频 \
    --Operator 16556266637489 \
    --SegmentGroupId 5fd6e20b0e1b530001f5daed \
    --SegmentIds seg_5fd6e20b0e1b530001f5daee
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

