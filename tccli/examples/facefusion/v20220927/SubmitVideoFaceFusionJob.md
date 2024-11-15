**Example 1: 视频人脸融合**



Input: 

```
tccli facefusion SubmitVideoFaceFusionJob --cli-unfold-argument  \
    --ProjectId 100646 \
    --MergeInfos.0.Url https://i2.sinaimg.cn/ty/nba/2015-07-05/U10236P6T12D7648505F44DT20150705114547.jpg \
    --ModelId qc_100646_154021_9
```

Output: 
```
{
    "Response": {
        "JobId": "C0a5EXaNR7JzGvlg",
        "EstimatedProcessTime": 30,
        "JobQueueLength": 1,
        "ReviewResultSet": [
            {
                "Category": "Politics",
                "Code": "0",
                "CodeDescription": "OK",
                "Suggestion": "PASS",
                "Confidence": 30,
                "DetailSet": [
                    {
                        "Field": "",
                        "Label": "丁俊晖",
                        "Confidence": 30,
                        "Suggestion": "PASS"
                    }
                ]
            }
        ],
        "RequestId": "83ecff39-2e4a-41d5-8562-1f8898326565"
    }
}
```

