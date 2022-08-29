**Example 1: 请求示例**



Input: 

```
tccli sms ReportConversion --cli-unfold-argument  \
    --SmsSdkAppId 1400000001 \
    --SerialNo 5000:1045710669157053657849499619 \
    --ConversionTime 1658310430
```

Output: 
```
{
    "Response": {
        "ReportConversionStatus": {
            "Code": "ok",
            "Message": "report success"
        },
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

