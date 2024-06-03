**Example 1: 生成修改个人手机号链接**

生成修改个人手机号链接，
此用户是通过 获取c端用户实名链接实名的，
调用方知道用户的 userId， 所以使用 UserId 的方式生成手机号变更链接
生成的链接是 APP 的方式，所以参数中 Endpoint 为 APP

Input: 

```
tccli ess CreateUserMobileChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Operator.ClientIp 8.8.8.8 \
    --UserId yDCZmUUckpy1jpdxUBBx43i4P29qekYx \
    --Endpoint APP \
    --UserData MjMwMDAwMTM4Mw==
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1717751037,
        "RequestId": "s1717146237659391990",
        "Url": "pages/guide/index?to=MOBILE_CHANGE_INTENTION&shortKey=yDCZiUv2ByIvoFcoDTfb&autoJumpBack=true"
    }
}
```

**Example 2: 使用二要素生成修改个人手机号链接**

使用二要素（姓名/证件号）生成修改个人手机号链接
此用户是通过 获取c端用户实名链接实名的，
调用方不知道用户的 userId，但是有用户的二要素信息（姓名和证件号）
此时需要传递参数UserAccountType 为 1，表示个人
生成的链接是 短链的方式，所以参数中 Endpoint 为 HTTP_SHORT_URL

Input: 

```
tccli ess CreateUserMobileChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Operator.ClientIp 8.8.8.8 \
    --UserAccountType 1 \
    --Name 典子谦 \
    --IdCardType ID_CARD \
    --IdCardNumber 620000198802020000 \
    --Endpoint HTTP_SHORT_URL \
    --UserData MjMwMDAwMTM4Mw==
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1717754432,
        "RequestId": "s1717149632556325434",
        "Url": "https://test.essurl.cn/qLAEUBG2s4"
    }
}
```

**Example 3: 使用二要素生成修改员工手机号链接**

使用二要素（姓名/证件号）生成修改员工手机号链接
此用户是通过 获取c端用户实名链接实名的，
调用方不知道用户的 userId，但是有用户的二要素信息（姓名和证件号）
此时需要传递参数UserAccountType 为 0，表示员工
生成的链接是 短链的方式，所以参数中 Endpoint 为 HTTP_SHORT_URL

Input: 

```
tccli ess CreateUserMobileChangeUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Operator.ClientIp 8.8.8.8 \
    --UserAccountType 0 \
    --Name 典子谦 \
    --IdCardType ID_CARD \
    --IdCardNumber 620000198802020000 \
    --Endpoint HTTP_SHORT_URL \
    --UserData MjMwMDAwMTM4Mw==
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1717754432,
        "RequestId": "s1717149632556325434",
        "Url": "https://test.essurl.cn/qHAEUjG2s4"
    }
}
```

