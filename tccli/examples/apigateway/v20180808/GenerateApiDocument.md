**Example 1: 下载sdk和api文档**



Input: 

```
tccli apigateway GenerateApiDocument --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --GenEnvironment release \
    --GenLanguage Python
```

Output: 
```
{
    "Response": {
        "Result": {
            "DocumentURL": "https://apigateway-document-sdk-xxxxx",
            "SdkURL": "https://apigateway-document-sdk-xxxxx"
        },
        "RequestId": "01c56ec2-6a40-46bc-bdf6-8b273d4bec93"
    }
}
```

