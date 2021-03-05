**Example 1: 获取画质重生任务结果**



Input: 

```
tccli ie DescribeMediaQualityRestorationTaskRusult --cli-unfold-argument  \
    --TaskId b8dc83ef-7ce4-4d76-94b5-a8cfe73d40e3
```

Output: 
```
{
    "Response": {
        "TaskResult": {
            "TaskId": "b8dc83ef-7ce4-4d76-94b5-a8cfe73d40e3",
            "SubTaskResult": [
                {
                    "DownloadUrl": "http://yayunhui-1251820392-1251820392.cos.ap-beijing.myqcloud.com/test/mqr_test1.mp4",
                    "Md5": "5adf8bd17a2239bfb1dc7172e51e34a1",
                    "ProgressRate": 100,
                    "StatusCode": 0,
                    "StatusMsg": "0",
                    "TaskName": "1080_five_all.mp4",
                    "FileInfo": {
                        "FileSize": 31254626,
                        "FileType": "mp4",
                        "Bitrate": 8323468,
                        "Duration": 30040,
                        "VideoInfoResult": [
                            {
                                "Stream": 0,
                                "Height": 2160,
                                "Bitrate": 7975062,
                                "Fps": "25/1",
                                "Codec": "h264",
                                "Duration": 30040,
                                "PixFormat": "yuv420p"
                            }
                        ],
                        "AudioInfoResult": [
                            {
                                "Stream": 1,
                                "Sample": 48000,
                                "Channel": 6,
                                "Codec": "aac",
                                "Bitrate": 341546,
                                "Duration": 30015
                            }
                        ]
                    }
                }
            ]
        },
        "RequestId": "request_id_1"
    }
}
```

