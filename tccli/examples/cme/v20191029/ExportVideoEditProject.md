**Example 1: 导出项目**



Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId cmepid_1111 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id testid
```

Output: 
```
{
    "Response": {
        "TaskId": "24820810452266399",
        "RequestId": "requestId"
    }
}
```

**Example 2: 导出视频指定码率为 3M bps**



Input: 

```
tccli cme ExportVideoEditProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId cmepid_1111 \
    --Definition 10 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id testid \
    --ExportExtensionArgs.VideoBitrate 3145728
```

Output: 
```
{
    "Response": {
        "TaskId": "1250000001-TFUSIONCME-24820810452266399",
        "RequestId": "requestId"
    }
}
```

