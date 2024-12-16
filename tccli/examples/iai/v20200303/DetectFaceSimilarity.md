**Example 1: 人脸相似度检测接口成功示例**



Input: 

```
tccli iai DetectFaceSimilarity --cli-unfold-argument  \
    --UrlA http://test.image.myqcloud.com/testA.jpg \
    --UrlB http://test.image.myqcloud.com/testB.jpg
```

Output: 
```
{
    "Response": {
        "Score": 0.999,
        "RequestId": "a8eb4545-a154-4f86-9510-57a8be9cae0c"
    }
}
```

**Example 2: 人脸相似度检测接口异常示例**



Input: 

```
tccli iai DetectFaceSimilarity --cli-unfold-argument  \
    --UrlA http://test.image.myqcloud.com/testA.jpg \
    --UrlB http://test.image.myqcloud.com/testB.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.FaceQualityNotQualified",
            "Message": "人脸图片质量不符要求。"
        },
        "RequestId": "788270e8-91b7-4c59-bd00-1af257b1e482"
    }
}
```

