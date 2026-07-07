**Example 1: 模型支持图像输入**

	
模型支持图像输入

Input: 

```
tccli clb TestModelInputModalities --cli-unfold-argument  \
    --Model gpt-5 \
    --ProviderKey sk-1111 \
    --AccessType PublicCustom \
    --ApiBase http://11.141.93.26:10000/v1
```

Output: 
```
{
    "Response": {
        "Model": "gpt-5",
        "ProbeDetails": [
            {
                "ErrorInfo": {
                    "ErrorStatus": "",
                    "HttpCode": 0,
                    "OriginalMessage": ""
                },
                "Modality": "image",
                "Status": "Supported"
            }
        ],
        "SupportedModalities": [
            "text"
        ],
        "RequestId": "1c31d4b4-f209-4866-99d0-25248db915aa"
    }
}
```

