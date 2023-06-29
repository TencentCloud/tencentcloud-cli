**Example 1: 渠道商生成修改子客企业二维码链接**

渠道商生成修改子客企业二维码链接

Input: 

```
tccli ess CreateChannelSubOrganizationModifyQrCode --cli-unfold-argument  \
    --Operator.UserId yDwFQU******CYtOQfzVk \
    --ApplicationId yDwFYUU*****UekPZF8PM7tLlo6p
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1684401637,
        "QrCodeUrl": "abc",
        "RequestId": "abc"
    }
}
```

