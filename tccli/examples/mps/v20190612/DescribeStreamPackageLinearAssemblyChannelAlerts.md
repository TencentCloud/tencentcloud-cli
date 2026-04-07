**Example 1: 请求示例**

查询线性组装频道告警信息。

Input: 

```
tccli mps DescribeStreamPackageLinearAssemblyChannelAlerts --cli-unfold-argument  \
    --ChannelId 66503E8E0000930000F3 \
    --StartTime 1590508800 \
    --EndTime 1590508900
```

Output: 
```
{
    "Response": {
        "Infos": {
            "ProgramAlertCounts": [
                {
                    "ProgramId": "66503E8E0000930000F4",
                    "ProgramName": "demo_program",
                    "Category": "PLAYBACK_WARNING",
                    "Count": 1,
                    "LastModifiedTime": 1590508810
                }
            ],
            "ProgramAlertInfos": [
                {
                    "ChannelId": "66503E8E0000930000F3",
                    "ChannelName": "demo_channel",
                    "ProgramId": "66503E8E0000930000F4",
                    "ProgramName": "demo_program",
                    "Code": 30002,
                    "Category": "PLAYBACK_WARNING",
                    "Message": "During the channel assembly, a mismatched 'resolution' was encountered in the 'demo_channel' channel. The discrepancy lies in the 'demo_group' group between the manifest of '1590508810531' at 'testStreaming_1336638_1.m3u8' with 'resolution' 852x480, and the manifest of 'Filler slate' at 'testStreaming_1336638_0.m3u8' with 'resolution' 426x240.",
                    "LastModifiedTime": 1590508810
                }
            ]
        },
        "RequestId": "req-xxx"
    }
}
```

