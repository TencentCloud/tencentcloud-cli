**Example 1: Querying the list of transcoding to adaptive bitrate streaming templates**



Input: 

```
tccli vod DescribeAdaptiveDynamicStreamingTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AdaptiveDynamicStreamingTemplateSet": [
            {
                "Definition": 1001,
                "Type": "Custom",
                "Name": "Transcoding to adaptive bitrate streaming template 1",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "PackageType": "hls",
                "DrmType": "",
                "VideoTrackTemplateSet": [
                    {
                        "Definition": 1001,
                        "Container": "mp4",
                        "Type": "Custom",
                        "Name": "Video track template 1",
                        "Comment": "",
                        "CreateTime": "2018-10-01T10:00:00Z",
                        "UpdateTime": "2018-10-01T10:00:00Z",
                        "Codec": "libx264",
                        "Fps": 25,
                        "Bitrate": 128,
                        "ResolutionAdaptive": "close",
                        "Width": 1080,
                        "Height": 960,
                        "FillType": "black"
                    }
                ],
                "AudioTrackTemplateSet": [
                    {
                        "Definition": 1001,
                        "Container": "m4a",
                        "Type": "Custom",
                        "Name": "Audio track template 1",
                        "Comment": "",
                        "CreateTime": "2018-10-01T10:00:00Z",
                        "UpdateTime": "2018-10-01T10:00:00Z",
                        "Codec": "libfdk_aac",
                        "Bitrate": 128,
                        "SampleRate": 44100,
                        "AudioChannel": 2
                    }
                ],
                "DisableHigherVideoBitrate": 1,
                "DisableHigherVideoResolution": 0
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

