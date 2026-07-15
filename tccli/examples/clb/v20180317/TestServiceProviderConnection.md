**Example 1: 探测模型是否健康**



Input: 

```
tccli clb TestServiceProviderConnection --cli-unfold-argument  \
    --Models deepseek-reasoner \
    --ProviderKey sk-40df882e447043fcaca5e0fce4af1db1 \
    --AccessType PublicCustom \
    --ModelProtocol deepseek \
    --ApiBase http://api.deepseek.com/v1 \
    --VerifySSL False
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "ErrorInfo": {
                    "ErrorStatus": "",
                    "HttpCode": 0,
                    "OriginalMessage": ""
                },
                "Model": "deepseek-reasoner",
                "Status": "Success",
                "TestConnectionRequest": {
                    "RequestBody": "",
                    "RequestHeaders": "",
                    "RequestUrl": ""
                }
            }
        ],
        "RequestId": "0dc8d1e6-9fd3-41c9-a39e-dbd3d16da611"
    }
}
```

