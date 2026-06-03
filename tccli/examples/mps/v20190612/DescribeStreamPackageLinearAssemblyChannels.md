**Example 1: 请求示例**

查询线性组装频道信息列表。

Input: 

```
tccli mps DescribeStreamPackageLinearAssemblyChannels --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
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
                        "PlaybackURL": "http://123456.ap-tokyo.streampackage.srclivepull.myqcloud.com/channel_assembly/6761180C89C8CFE2334C/master.m3u8"
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
                "Id": "6761180C89C8CFE2334C",
                "Region": "ap-tokyo",
                "State": "Running",
                "TimeShiftEnable": false,
                "CreateTime": 1739263386
            }
        ],
        "PageNum": 1,
        "PageSize": 1,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "req-xxx"
    }
}
```

