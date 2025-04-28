**Example 1: 获取视频信息**



Input: 

```
tccli mps DescribeMediaMetaData --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88 \
    --InputInfo.CosInputInfo.Region ap-chongqing \
    --InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov
```

Output: 
```
{
    "Response": {
        "MetaData": {
            "AudioDuration": 380.9465637207031,
            "AudioStreamSet": [
                {
                    "Bitrate": 95999,
                    "Codec": "aac",
                    "Codecs": "mp4a.40.2",
                    "Loudness": 0,
                    "Channel": 2,
                    "SamplingRate": 44100
                }
            ],
            "Bitrate": 409657,
            "Container": "mov,mp4,m4a,3gp,3g2,mj2",
            "Duration": 380.9465637207031,
            "Height": 360,
            "Rotate": 0,
            "Size": 19626862,
            "VideoDuration": 380.8804931640625,
            "VideoStreamSet": [
                {
                    "Bitrate": 313658,
                    "Codec": "h264",
                    "Codecs": "avc1.ffe100",
                    "ColorPrimaries": "",
                    "ColorSpace": "",
                    "ColorTransfer": "",
                    "HdrType": "",
                    "Fps": 29,
                    "Height": 360,
                    "Width": 480
                }
            ],
            "Width": 480
        },
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

