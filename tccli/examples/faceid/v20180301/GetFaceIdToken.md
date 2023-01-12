**Example 1: 获取token成功**

获取 SDK 核验 token

Input: 

```
tccli faceid GetFaceIdToken --cli-unfold-argument  \
    --CompareLib BUSINESS \
    --IdCard xxxxxxxxxxxxxxxxx \
    --Name xxxxxxxxxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "FaceIdToken": "asdasdadasdasd",
        "RequestId": "94b54cdf-d975-4718-b091-32f8d79d6397"
    }
}
```

