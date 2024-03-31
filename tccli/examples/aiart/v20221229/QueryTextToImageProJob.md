**Example 1: 成功调用**

成功调用

Input: 

```
tccli aiart QueryTextToImageProJob --cli-unfold-argument  \
    --JobId testJobId
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "5",
        "JobStatusMsg": "处理完成",
        "RequestId": "fae816f9-7fd1-4e39-bf1c-3d43677603de",
        "ResultDetails": [
            "Success"
        ],
        "ResultImage": [
            "https://test.jpg"
        ]
    }
}
```

