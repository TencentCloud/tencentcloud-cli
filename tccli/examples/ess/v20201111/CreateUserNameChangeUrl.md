**Example 1: 生成个人更名链接**

生成个人通用更名链接

Input: 

```
tccli ess CreateUserNameChangeUrl --cli-unfold-argument  \
    --Operator.UserId 19561039c9***********32520fde6a \
    --Operator.ClientIp 8.8.8.8 \
    --Endpoint HTTP \
    --UserData TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5LCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1748247333,
        "MiniAppId": "",
        "RequestId": "s1747642533895017639",
        "UserVerifyUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=MP_PERSONAL_VERIFY&shortKey=yDttYU******bLXcb"
    }
}
```

