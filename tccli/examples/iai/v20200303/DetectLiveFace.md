**Example 1: Detecting liveness based on image**



Input: 

```
tccli iai DetectLiveFace --cli-unfold-argument  \
    --Url http://test.image.myqcloud.com/testA.jpg
```

Output: 
```
{
    "Response": {
        "Score": 99,
        "IsLiveness": true,
        "FaceModelVersion": "3.0",
        "RequestId": "048a5eb3-f7a9-4c1f-a982-00e90b6b892c"
    }
}
```

