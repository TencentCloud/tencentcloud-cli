**Example 1: 获取任务详情**

 获取任务详情。

Input: 

```
tccli cme DescribeTaskDetail --cli-unfold-argument  \
    --Platform test \
    --TaskId 181xxxxxxxx9-procedurev2-b718fcee09a72470bf665cf55351d810t0
```

Output: 
```
{
    "Response": {
        "CreateTime": "2020-04-28T18:16:58Z",
        "ErrCode": 0,
        "ErrMsg": "Success.",
        "Progress": 100,
        "RequestId": "85b8cdac-8e18-430a-aeae-08076ac26a11",
        "Status": "SUCCESS",
        "TaskType": "VIDEO_EDIT_PROJECT_EXPORT",
        "VideoEditProjectOutput": {
            "MaterialId": "6866c9a7-a2ca-4d",
            "MetaData": {
                "AudioStreamInfoSet": [
                    {
                        "Bitrate": 46552,
                        "Codec": "aac",
                        "SamplingRate": 16000
                    }
                ],
                "Bitrate": 6917072,
                "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                "Duration": 346.55999755859375,
                "Height": 1080,
                "Rotate": 0,
                "Size": 299688882,
                "VideoStreamInfoSet": [
                    {
                        "Bitrate": 6870520,
                        "Codec": "h264",
                        "Fps": 25,
                        "Height": 1080,
                        "Width": 1920
                    }
                ],
                "Width": 1920
            },
            "URL": "http://cmedemo.vod2.myqcloud.com/xxxxx/cemdemo.mp4",
            "VodFileId": "5285890802029089"
        }
    }
}
```

