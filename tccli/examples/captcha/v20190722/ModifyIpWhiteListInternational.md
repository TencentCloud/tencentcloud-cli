**Example 1: 编辑Ip白名单**



Input: 

```
tccli captcha ModifyIpWhiteListInternational --cli-unfold-argument  \
    --Name 内网测试 \
    --Status 1 \
    --Id 1 \
    --Comment 内网测试 \
    --CaptchaAppid 1
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "CaptchaCode": 0,
        "CaptchaMsg": "success",
        "RequestId": "c634b435-7bfe-4f04-b447-b995a2dd8adb"
    }
}
```

