**Example 1: 调用返回成功**



Input: 

```
tccli facefusion FaceFusionLite --cli-unfold-argument  \
    --ProjectId 100646 \
    --ModelId qc_100646_154021_9 \
    --MergeInfos.0.Url https://test-139.cos.ap-nan.cloud.com/bk.jpeg
```

Output: 
```
{
    "Response": {
        "Image": "https://facefusion-1254418846.cos.ap-guangzhou.myqcloud.com/qc_100646_204857_1_1543312645513131155.jpg",
        "RequestId": "66676130-5588-4cdb-a81e-8bd3c99cea1f",
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
        ]
    }
}
```

