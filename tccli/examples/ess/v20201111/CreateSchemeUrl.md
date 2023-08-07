**Example 1: 获取小程序跳转链接**

获取小程序跳转链接

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowId 1956103*****20fde6a \
    --PathType 1 \
    --Name 张三 \
    --Mobile 13888888888 \
    --OrganizationName 测试企业 \
    --EndPoint HTTP \
    --AutoJumpBack False \
    --Operator.UserId 00033e********4aa82a9
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

**Example 2: 获取小程序跳转链接(隐藏按钮)**

隐藏合同签署页面更多操作按钮和签署成功页的查看详情按钮

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowId 1956103*****20fde6a \
    --PathType 1 \
    --Name 张三 \
    --Mobile 13888888888 \
    --OrganizationName 测试企业 \
    --EndPoint HTTP \
    --AutoJumpBack False \
    --Operator.UserId 00033e********4aa82a9 \
    --Hides 0 3
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

