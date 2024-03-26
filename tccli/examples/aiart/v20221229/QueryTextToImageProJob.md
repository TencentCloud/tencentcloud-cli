**Example 1: 成功调用**

成功调用

Input: 

```
tccli aiart QueryTextToImageProJob --cli-unfold-argument  \
    --JobId 251241601-1711361138-3acbb363-ea8f-11ee-9e92-525400047e59-0
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
            "https://aiart-1258344699.cos.ap-guangzhou.myqcloud.com/text_to_img_pro/251241601/251241601-1711361138-3acbb363-ea8f-11ee-9e92-525400047e59-0/1?q-sign-algorithm=sha1&q-ak=AKIDpRovliU1IJ5ctufBSVIq8AwTlnZ5MN8d&q-sign-time=1711361147%3B1711364747&q-key-time=1711361147%3B1711364747&q-header-list=host&q-url-param-list=&q-signature=27a9cbeacebe4bb14da176f3489ef26d84cec2fc"
        ]
    }
}
```

