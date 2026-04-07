**Example 1: 请求示例**

创建线性组装Program。

Input: 

```
tccli mps CreateStreamPackageLinearAssemblyProgram --cli-unfold-argument  \
    --Name demo_program \
    --AttachedChannel 66503E8E0000930000F3 \
    --SourceType VOD \
    --SourceLocationId 66503E8E0000930000F0 \
    --SourceName vod_source \
    --PlaybackConf.TransitionType Relative \
    --PlaybackConf.StartTime 0 \
    --PlaybackConf.Duration 0 \
    --PlaybackConf.RelativePosition After \
    --PlaybackConf.RelativeProgramId 66503E8E0000930000F7 \
    --PlaybackConf.ClipRangeConf.Type Entire \
    --PlaybackConf.ClipRangeConf.Offset 0 \
    --AdBreaks.0.SourceLocationId 66503E8E0000930000F1 \
    --AdBreaks.0.VodSourceName ad_source \
    --AdBreaks.0.Offset 64000 \
    --AdBreaks.0.MessageType SpliceInsert \
    --AdBreaks.0.SpliceInsertConf.EventID 1 \
    --AdBreaks.0.SpliceInsertConf.AvailNum 0 \
    --AdBreaks.0.SpliceInsertConf.AvailExpected 0 \
    --AdBreaks.0.SpliceInsertConf.ProgramID 3 \
    --AdBreaks.0.Metadatas.0.Key test-key \
    --AdBreaks.0.Metadatas.0.Value test-value \
    --AdBreaks.0.SourceLocationName ad_location
```

Output: 
```
{
    "Response": {
        "Info": {
            "Name": "demo_program",
            "SourceType": "VOD",
            "SourceLocationId": "66503E8E0000930000F0",
            "SourceId": "66503E8E0000930000F1",
            "SourceName": "vod_source",
            "AttachedChannel": "66503E8E0000930000F2",
            "PlaybackConf": {
                "Duration": 0,
                "TransitionType": "Relative",
                "StartTime": 0,
                "RelativePosition": "After",
                "RelativeProgramId": "66503E8E0000930000F3",
                "ClipRangeConf": {
                    "Type": "Entire",
                    "Offset": 0
                },
                "RelativeProgramName": "relative_program"
            },
            "AdBreaks": [
                {
                    "SourceLocationId": "66503E8E0000930000F4",
                    "VodSourceName": "ad_source",
                    "Offset": 64000,
                    "MessageType": "SpliceInsert",
                    "SpliceInsertConf": {
                        "EventID": "1",
                        "AvailNum": "0",
                        "AvailExpected": "0",
                        "ProgramID": "3"
                    },
                    "Metadatas": [
                        {
                            "Key": "test-key",
                            "Value": "test-value"
                        }
                    ],
                    "SourceLocationName": "ad_location"
                }
            ],
            "Id": "66503E8E0000930000F5",
            "Region": "ap-singapore",
            "SourceLocationName": "demo_location"
        },
        "RequestId": "req-xxx"
    }
}
```

