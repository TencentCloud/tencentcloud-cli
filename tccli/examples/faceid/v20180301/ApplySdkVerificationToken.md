**Example 1: ApplySdkVerificationToken 示例**

指定重试次数调用成功

Input: 

```
tccli faceid ApplySdkVerificationToken --cli-unfold-argument  \
    --CheckMode 3 \
    --RetryLimit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e43ab16a-6eb3-4fc0-8e44-f594f7dc2c20",
        "SdkToken": "C736CEB2-03D89-014A10-B17B-B2DC535CA53B"
    }
}
```

