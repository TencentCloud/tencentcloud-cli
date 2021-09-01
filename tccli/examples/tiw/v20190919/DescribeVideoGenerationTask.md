**Example 1: 查询录制视频生成**



Input: 

```
tccli tiw DescribeVideoGenerationTask --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --TaskId ghucnligqtgtvk2624mb
```

Output: 
```
{
    "Response": {
        "GroupId": "900822",
        "Progress": 100,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851",
        "RoomId": 900822,
        "Status": "FINISHED",
        "TaskId": "00e1jv8ve0jcqk7da9lb",
        "TotalTime": 156750,
        "VideoInfoList": [
            {
                "UserId": "",
                "VideoDuration": 156750,
                "VideoFormat": "mp4",
                "VideoId": "5285890792776509100",
                "VideoPlayTime": 0,
                "VideoSize": 318384,
                "VideoType": 2,
                "Width": 1024,
                "Height": 768,
                "VideoUrl": "http://1257240443.vod2.myqcloud.com/cc35b442vodcq1257240443/video.mp4"
            }
        ],
        "VideoInfos": {
            "VideoType": 0,
            "VideoUrl": "已废弃，请使用VideoInfoList",
            "UserId": "xx",
            "VideoId": "xx",
            "VideoSize": 0,
            "VideoDuration": 0,
            "Width": 0,
            "Height": 0,
            "VideoPlayTime": 0,
            "VideoFormat": "xx"
        }
    }
}
```

