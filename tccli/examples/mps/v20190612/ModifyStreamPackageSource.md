**Example 1: 请求示例**

修改媒体包装Source信息。

Input: 

```
tccli mps ModifyStreamPackageSource --cli-unfold-argument  \
    --Id 698A9AAB1D3EA5F03229 \
    --Name test_source_2 \
    --Type VOD \
    --PackageConfs.0.GroupName group_name \
    --PackageConfs.0.Type HLS \
    --PackageConfs.0.Path /vod/main.m3u8 \
    --SourceTags.0.Key SPORT \
    --SourceTags.0.Value sport
```

Output: 
```
{
    "Response": {
        "RequestId": "5a0d7180-4579-49a9-a0f0-c22602b3b0f7"
    }
}
```

