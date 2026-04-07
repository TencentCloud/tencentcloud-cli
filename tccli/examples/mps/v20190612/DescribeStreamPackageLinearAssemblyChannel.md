**Example 1: 请求示例**

查询媒体包装线性组装频道信息。

Input: 

```
tccli mps DescribeStreamPackageLinearAssemblyChannel --cli-unfold-argument  \
    --Id 66503E8E0000930000F3
```

Output: 
```
{
    "Response": {
        "Info": {
            "Name": "demo_channel",
            "Tier": "Standard",
            "PlaybackMode": "Linear",
            "SlateConf": {
                "SourceLocationId": "6760EC9700006786ABB0",
                "VodSourceName": "slate_vod_1"
            },
            "Outputs": [
                {
                    "Type": "HLS",
                    "GroupName": "source_group_1",
                    "ManifestName": "master",
                    "ManifestConf": {
                        "Windows": 60,
                        "AdMarkupType": "Enhanced SCTE-35"
                    },
                    "PlaybackURL": "http://123456.ap-tokyo.streampackage.srcli****ll.myqcloud.com/channel_ass**bly/6761180C89C8CFE2334C/ma*ter.m3u8"
                }
            ],
            "AttachedPrograms": [
                "67612E1189C8D039B3F6"
            ],
            "ProgramSchedules": [
                {
                    "ProgramName": "demo_program",
                    "ProgramId": "67612E1189C8D039B3F6",
                    "SourceType": "Vod",
                    "SourceId": "67613EEB0000B2AC7ED5",
                    "SourceLocationId": "6760EC9700006786ABB0",
                    "StartTime": 1739265386,
                    "Duration": "60000"
                }
            ],
            "Id": "66503E8E0000930000F3",
            "Region": "ap-tokyo",
            "State": "Running",
            "TimeShiftEnable": false,
            "CreateTime": 1739263386
        },
        "RequestId": "7d4b42b2-a5d4-499e-ac9b-cdabd9b46026"
    }
}
```

