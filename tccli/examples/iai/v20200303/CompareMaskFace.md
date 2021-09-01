**Example 1: 人脸比对接口**



Input: 

```
tccli iai CompareMaskFace --cli-unfold-argument  \
    --UrlA http://test.image.myqcloud.com/testA.jpg \
    --UrlB http://test.image.myqcloud.com/testB.jpg
```

Output: 
```
{
    "Response": {
        "Score": 0.999,
        "FaceModelVersion": "3.0",
        "RequestId": "a8eb4545-a154-4f86-9510-57a8be9cae0c"
    }
}
```

