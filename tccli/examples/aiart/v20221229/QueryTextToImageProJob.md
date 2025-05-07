**Example 1: 成功调用**

成功调用

Input: 

```
tccli aiart QueryTextToImageProJob --cli-unfold-argument  \
    --JobId 251197749-1732000967-13b82f68-a647-11ef-be80-525400047e59-0
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
            "https://aiart-xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg?q-sign-algorithm=sha1&q-ak=xxxxx&q-sign-time=1731574045;1731577645&q-key-time=1731574045;1731577645&q-header-list=host&q-url-param-list=&q-signature=31fe75c1c18c3d91db59508961209dd37aaf41c7"
        ],
        "RevisedPrompt": [
            "动漫风格，画面主要描述一个雨天的场景，一位亚洲男孩在雨中独自行走，他的身姿显得有些落寞，背景是一个阴雨连绵的城市，镜头是中景"
        ]
    }
}
```

