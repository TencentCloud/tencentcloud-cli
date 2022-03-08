**Example 1: 获取小程序跳转链接**

获取小程序跳转链接

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowId 1956103*****20fde6a \
    --PathType 1 \
    --Name 国大橙子 \
    --Mobile 13888888888 \
    --Operator.UserId 00033e********4aa82a9 \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Operator.ProxyIp 
```

Output: 
```
{
    "Response": {
        "SchemeUrl": "weixin://dl/business/?t= *TICKET*",
        "RequestId": ""
    }
}
```

