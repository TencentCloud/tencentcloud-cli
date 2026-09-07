**Example 1: 控制台新增Ip白名单**



Input: 

```
tccli captcha CreateIpWhiteListInternational --cli-unfold-argument  \
    --Name abc \
    --CaptchaAppid 179000003 \
    --Ip 127.0.0.1 \
    --Comment abc
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "CaptchaCode": 0,
        "CaptchaMsg": "",
        "RequestId": "637bbeab-43c8-4074-96af-0d0e66f95ba0",
        "IdList": [
            2100000000
        ]
    }
}
```

