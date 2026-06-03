**Example 1: 请求示例**

修改媒体包装Program信息。

Input: 

```
tccli mps ModifyStreamPackageLinearAssemblyProgram --cli-unfold-argument  \
    --Id 67612E1189C8D039B3F6 \
    --Name demo \
    --SourceType vod_source \
    --SourceLocationId 6760EC9700006786ABB0 \
    --SourceName vod1 \
    --PlaybackConf.TransitionType Relative \
    --PlaybackConf.RelativePosition After \
    --PlaybackConf.RelativeProgramId 67612E1189E3D039B3F6 \
    --PlaybackConf.ClipRangeConf.Type SpecifyTimeRange \
    --PlaybackConf.ClipRangeConf.Offset 30000 \
    --AdBreaks.0.SourceLocationId 6760EC9700006786ABB0 \
    --AdBreaks.0.VodSourceName ad_1 \
    --AdBreaks.0.Offset 0 \
    --AdBreaks.0.MessageType SpliceInsert \
    --AdBreaks.0.SpliceInsertConf.EventID 0 \
    --AdBreaks.0.SpliceInsertConf.AvailNum 0 \
    --AdBreaks.0.SpliceInsertConf.AvailExpected 1 \
    --AdBreaks.0.SpliceInsertConf.ProgramID 0 \
    --AdBreaks.0.Metadatas.0.Key key1 \
    --AdBreaks.0.Metadatas.0.Value value1 \
    --AdBreaks.0.SourceLocationName demo_source_location
```

Output: 
```
{
    "Response": {
        "RequestId": "7d4b42b2-a5d4-499e-ac9b-cdabd9b46026"
    }
}
```

