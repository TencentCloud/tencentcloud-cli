**Example 1: 渠道商生成修改子客企业二维码链接**

渠道商生成修改子客企业二维码链接

Input: 

```
tccli ess CreateChannelSubOrganizationModifyQrCode --cli-unfold-argument  \
    --Operator.UserId yDwFQUUckpswii3uUEwyEKVCYtOQfzVk \
    --Operator.Channel TENCENTCLOUD \
    --Operator.OpenId yDwFQUUckpsw6tpgUuMcjx2yLwQhEm9k \
    --Operator.ClientIp 59.37.125.125 \
    --ApplicationId yDwFYUUckpsywy56UekPZF8PM7tLlo6p
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

