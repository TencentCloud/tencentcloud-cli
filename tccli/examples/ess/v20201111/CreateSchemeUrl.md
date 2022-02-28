**Example 1: 获取小程序跳转链接**

获取小程序跳转链接

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowId dasdai2231289d1daslkdjasqqok \
    --PathType 1 \
    --Name 国大橙子 \
    --Mobile 13888888888 \
    --Operator.UserId 65fb0c591044be8a1f60aa382cc5ed0e \
    --Operator.ClientIp  \
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

