**Example 1: 请求示例**

创建媒体包装频道。

Input: 

```
tccli mps CreateStreamPackageLinearAssemblyChannel --cli-unfold-argument  \
    --Name test_channel \
    --Tier Standard \
    --PlaybackMode Linear \
    --TimeShiftEnable True \
    --TimeShiftConf.TimeWindows 10 \
    --SlateConf.SourceLocationId 698557DC1D3EA60266EB \
    --SlateConf.VodSourceName test_source_2 \
    --Outputs.0.Type HLS \
    --Outputs.0.GroupName group_name \
    --Outputs.0.ManifestName master \
    --Outputs.0.ManifestConf.Windows 60 \
    --Outputs.0.ManifestConf.AdMarkupType Enhanced SCTE-35 \
    --Outputs.0.DashManifestConf.Windows 60 \
    --Outputs.0.DashManifestConf.MinBufferTime 30 \
    --Outputs.0.DashManifestConf.MinUpdatePeriod 10 \
    --Outputs.0.DashManifestConf.SuggestedPresentationDelay 10
```

Output: 
```
{
    "Response": {
        "Info": {
            "AttachedPrograms": [],
            "CreateTime": 1770692416,
            "Id": "698A9F401D3EA6831FD9",
            "Name": "test_channel",
            "Outputs": [
                {
                    "DashManifestConf": {
                        "MinBufferTime": 0,
                        "MinUpdatePeriod": 0,
                        "SuggestedPresentationDelay": 0,
                        "Windows": 0
                    },
                    "GroupName": "group_name",
                    "ManifestConf": {
                        "AdMarkupType": "Enhanced SCTE-35",
                        "Windows": 60
                    },
                    "ManifestName": "master",
                    "PlaybackURL": "http://25100****.ap-shanghai.streampack***.srclivepull.myqcloud.com/channel*******ly/698A9F401D3EA68*****/****er.m3u8",
                    "Type": "HLS"
                }
            ],
            "PlaybackMode": "Linear",
            "ProgramSchedules": [],
            "Region": "ap-shanghai",
            "SlateConf": {
                "SourceLocationId": "698557DC1D3EA60266EB",
                "VodSourceName": "test_source_2"
            },
            "State": "IDLE",
            "Tier": "Standard",
            "TimeShiftConf": {
                "TimeWindows": 10
            },
            "TimeShiftEnable": true
        },
        "RequestId": "3aebd063-df23-4efe-b51d-845eac508efb"
    }
}
```

