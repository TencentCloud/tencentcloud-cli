**Example 1: 创建白板板书生成任务**



Input: 

```
tccli tiw CreateSnapshotTask --cli-unfold-argument  \
    --COS.TargetDir snapshot/ \
    --COS.Region ap-guangzhou \
    --COS.Bucket test-123070000 \
    --COS.Domain xxx.file.com \
    --COS.Uin 130001358 \
    --Whiteboard.Width 1280 \
    --Whiteboard.InitParams {"ratio":"16:9"} \
    --Whiteboard.Height 720 \
    --RoomId 12345 \
    --SdkAppId 1400123480 \
    --CallbackURL http://xx/callback
```

Output: 
```
{
    "Response": {
        "TaskID": "d1806f20-25b8-4c30-8176-c0832bf84e02",
        "RequestId": "fe36df20-25b8-4c30-8176-cff28afacb25"
    }
}
```

