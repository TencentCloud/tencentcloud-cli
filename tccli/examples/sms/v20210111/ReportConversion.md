**Example 1: 请求示例**



Input: 

```
tccli sms ReportConversion --cli-unfold-argument  \
    --SmsSdkAppId 1400000001 \
    --SerialNo a12gb4e2-sd11-5dx6-aav9-8f3d97xa2xu7 \
    --ConversionTime 1658310430
```

Output: 
```
{
    "Response": {
        "ReportConversionStatus": {
            "Code": "OK",
            "Message": "success"
        },
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

