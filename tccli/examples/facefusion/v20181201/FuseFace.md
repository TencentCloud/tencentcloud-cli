**Example 1: 人脸融合-选脸融合**



Input: 

```
tccli facefusion FuseFace --cli-unfold-argument  \
    --ProjectId 300029 \
    --ModelId qc_300029_453345_1 \
    --RspImgType url \
    --MergeInfos.0.Image /9/242342342342 \
    --MergeInfos.0.Url http://test.image.myqcloud.com/testB.jpg \
    --MergeInfos.0.InputImageFaceRect.X 1 \
    --MergeInfos.0.InputImageFaceRect.Y 2 \
    --MergeInfos.0.InputImageFaceRect.Width 11 \
    --MergeInfos.0.InputImageFaceRect.Height 22 \
    --MergeInfos.0.TemplateFaceID 1 \
    --FuseProfileDegree 1 \
    --FuseFaceDegree 1
```

Output: 
```
{
    "Response": {
        "FusedImage": "/9/tetwtwe",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
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

