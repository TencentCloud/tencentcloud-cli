**Example 1: 人脸静态活体检测（高精度版）接口**



Input: 

```
tccli iai DetectLiveFaceAccurate --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg
```

Output: 
```
{
    "Response": {
        "Score": 99,
        "FaceModelVersion": "3.0",
        "RequestId": "048a5eb3-f7a9-4c1f-a982-00e90b6b892c"
    }
}
```

