**Example 1: 修改编码配置名称**



Input: 

```
tccli cme ModifyVideoEncodingPreset --cli-unfold-argument  \
    --Platform test \
    --Name test1 \
    --Id 100048
```

Output: 
```
{
    "Response": {
        "RequestId": "4e6ab84c-47c5-45af-8f47-ec39eaf0606d"
    }
}
```

**Example 2: 修改编码配置中的视频尺寸**



Input: 

```
tccli cme ModifyVideoEncodingPreset --cli-unfold-argument  \
    --Platform test \
    --Id 100048 \
    --VideoSetting.ShortEdge 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "7164f965-2923-4640-9010-05c51b282433"
    }
}
```

