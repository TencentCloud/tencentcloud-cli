**Example 1: 请求示例**

修改媒体包装Source信息。

Input: 

```
tccli mps ModifyStreamPackageLinearAssemblyChannel --cli-unfold-argument  \
    --Id 698A9F401D3EA6831FD9 \
    --Name test_channel \
    --Tier Standard \
    --PlaybackMode Linear \
    --TimeShiftEnable True \
    --SlateConf.SourceLocationId 698557DC1D3EA60266EB \
    --SlateConf.VodSourceName test_source_2 \
    --Outputs.0.Type HLS \
    --Outputs.0.GroupName group_name \
    --Outputs.0.ManifestName master \
    --Outputs.0.ManifestConf.Windows 60 \
    --Outputs.0.ManifestConf.AdMarkupType Enhanced SCTE-35 \
    --Outputs.0.PlaybackURL http://**100***8.ap-shanghai.streampa**age.srcl*****ll.myqcloud.com/****nel_assembly/698A9F40*****6831FD9/master.m3u8 \
    --Outputs.0.DashManifestConf.Windows 0 \
    --Outputs.0.DashManifestConf.MinBufferTime 0 \
    --Outputs.0.DashManifestConf.MinUpdatePeriod 0 \
    --Outputs.0.DashManifestConf.SuggestedPresentationDelay 0
```

Output: 
```
{
    "Response": {
        "RequestId": "44a14b7a-8589-48d2-b392-087f18f458df"
    }
}
```

