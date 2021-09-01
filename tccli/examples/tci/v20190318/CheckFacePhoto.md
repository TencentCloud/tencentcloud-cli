**Example 1: 检查人脸图片**

检查输入人脸图片 url 是否合规

Input: 

```
tccli tci CheckFacePhoto --cli-unfold-argument  \
    --FileContent https%3A%2F%2Fedu-test-1253131631.cos.ap-guangzhou.myqcloud.com%2Faieduautotest%2Fautotest_facea.png \
    --FileType picture_url
```

Output: 
```
{
    "Response": {
        "RequestId": "7f07c9c3-d7e1-47ee-89ed-f08267d6b39d",
        "CheckResult": 0
    }
}
```

