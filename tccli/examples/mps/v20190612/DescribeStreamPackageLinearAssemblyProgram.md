**Example 1: 请求示例**

查询媒体包装Program信息。

Input: 

```
tccli mps DescribeStreamPackageLinearAssemblyProgram --cli-unfold-argument  \
    --Id 66503E8E0000930000F5
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

