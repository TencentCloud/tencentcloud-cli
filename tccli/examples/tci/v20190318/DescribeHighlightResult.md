**Example 1: 视频精彩集锦评估结果详情查询**

查询通过SubmitHighlights接口提交的精彩集锦剪辑任务的结果。

Input: 

```
tccli tci DescribeHighlightResult --cli-unfold-argument  \
    --JobId 97
```

Output: 
```
{
    "Response": {
        "JobId": 97,
        "Process": 100,
        "HighlightsInfo": [
            {
                "FaceId": "2258353436553278",
                "HighlightsUrl": "http://videowonderful-1255701415.cos.ap-guangzhou.myqcloud.com/test/20190315_201544--ef_wonderful_20190315_201542_2258353436553278.mp4?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1552652149%3B1552652209%26q-key-time%3D1552652149%3B1552652209%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D07e26350266823e5736a17945d2794ec0bcc8d66",
                "Smile": [
                    {
                        "StartTime": 48000,
                        "EndTime": 83000
                    },
                    {
                        "StartTime": 339000,
                        "EndTime": 419000
                    },
                    {
                        "StartTime": 1027000,
                        "EndTime": 1036000
                    },
                    {
                        "StartTime": 1311000,
                        "EndTime": 1320000
                    },
                    {
                        "StartTime": 1443000,
                        "EndTime": 1482000
                    }
                ],
                "Concentration": null
            }
        ],
        "RequestId": "f571fd7c-131f-459f-93ec-c0605da0bfd9"
    }
}
```

