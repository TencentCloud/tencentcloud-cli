**Example 1: 获取 MPS 任务的参数模板列表**



Input: 

```
tccli vod DescribeMPSTemplates --cli-unfold-argument  \
    --SubAppId 1500000001 \
    --TemplateType Transcode \
    --MPSDescribeTemplateParams {"Definitions": [100010],"Type": "Custom"}
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MPSTemplateSet": [
            {
                "TaskType": "Transcode",
                "MPSTemplateInfo": "{\"Definition\":\"100010\",\"Container\":\"mp4\",\"Name\":\"test\",\"Comment\":\"\",\"Type\":\"Custom\",\"RemoveVideo\":0,\"RemoveAudio\":0,\"VideoTemplate\":{\"Codec\":\"h264\",\"Fps\":0,\"Bitrate\":0,\"ResolutionAdaptive\":\"open\",\"Width\":0,\"Height\":0,\"FillType\":\"black\",\"Gop\":0,\"VideoProfile\":\"\",\"VideoLevel\":\"\",\"Subjective\":0,\"ContentAdaptStream\":0,\"SegmentType\":0,\"FpsDenominator\":1,\"Stereo3dType\":\"\",\"HlsTime\":0,\"Mode\":\"VBR\",\"Sar\":\"\",\"NoScenecut\":0,\"BitDepth\":8,\"RawPts\":0,\"ScenarioBased\":0,\"SceneType\":\"\",\"CompressType\":\"\"},\"AudioTemplate\":{\"Codec\":\"aac\",\"Bitrate\":0,\"SampleRate\":44100,\"AudioChannel\":2,\"StreamSelects\":[]},\"ContainerType\":\"Video\",\"CreateTime\":\"2025-07-22T20:28:36+08:00\",\"UpdateTime\":\"2025-07-22T20:28:36+08:00\",\"TEHDConfig\":null,\"EnhanceConfig\":{\"VideoEnhance\":{\"FrameRate\":{\"Switch\":\"ON\",\"Fps\":0},\"SuperResolution\":{\"Switch\":\"ON\",\"Type\":\"hq\",\"Size\":2},\"Hdr\":{\"Switch\":\"OFF\",\"Type\":\"HDR10\"},\"Denoise\":{\"Switch\":\"OFF\",\"Type\":\"weak\"},\"ImageQualityEnhance\":{\"Switch\":\"ON\",\"Type\":\"normal\"},\"ColorEnhance\":{\"Switch\":\"ON\",\"Type\":\"weak\"},\"SharpEnhance\":{\"Switch\":\"OFF\",\"Intensity\":0},\"FaceEnhance\":{\"Switch\":\"OFF\",\"Intensity\":0},\"LowLightEnhance\":{\"Switch\":\"OFF\",\"Type\":\"normal\"},\"ScratchRepair\":{\"Switch\":\"OFF\",\"Intensity\":0},\"ArtifactRepair\":{\"Switch\":\"OFF\",\"Type\":\"weak\"}},\"AudioEnhance\":{\"Denoise\":{\"Switch\":\"OFF\"},\"Separate\":{\"Switch\":\"OFF\",\"Type\":\"normal\",\"Track\":\"vocal\"},\"VolumeBalance\":{\"Switch\":\"OFF\",\"Type\":\"loudNorm\"},\"Beautify\":{\"Switch\":\"OFF\",\"Types\":[\"declick\"]}}},\"StdExtInfo\":null,\"AliasName\":\"\"}"
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

