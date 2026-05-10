**Example 1: GetFaceIdTokenIntl 示例**

指定活体重试次数，调用成功

Input: 

```
tccli faceid GetFaceIdTokenIntl --cli-unfold-argument  \
    --CheckMode liveness \
    --RetryLimit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ace1147a-d761-49a2-a180-0c95263b50ff",
        "SdkToken": "C8CFF283-539AF-014E77-A5CF-DD9CAD93EFE2"
    }
}
```

