**Example 1: 获取某个合同组的签署链接(短链)**

1. 获取合同组的签署链接(FlowGroupId设置成合同组的ID)
2. 签署链接是短链(EndPoint设置成HTTP_SHORT_URL)

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowGroupId yDwq7UUckpknjh4hUu1vFD6uHSIyKQPf \
    --PathType 1 \
    --Name 典子谦 \
    --Mobile 13200000000 \
    --EndPoint HTTP_SHORT_URL \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj
```

Output: 
```
{
    "Response": {
        "RequestId": "s1693796254269814638",
        "SchemeUrl": "https://essurl.cn/i3am**5Y9W"
    }
}
```

**Example 2: 获取某个流程合同的小程序跳转签署链接**

1.链接是在 第三方APP或小程序中使用(EndPoint设置成APP)
2.签署完成后自动跳回第三方APP或小程序 (AutoJumpBack设置成true)


Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowId yDwq7UU*Uu1vFD6uHSIyKQPf \
    --PathType 1 \
    --Name 典子谦 \
    --Mobile 13200000000 \
    --EndPoint APP \
    --AutoJumpBack True \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj
```

Output: 
```
{
    "Response": {
        "RequestId": "s1693795766610672060",
        "SchemeUrl": "pages/guide?from=default&where=mini&id=yDwq7UU*Uu1vFD6uHSIyKQPf&to=CONTRACT_DETAIL&name=%E5%91%&phone=MTkx**0OTc3NjA%3D&autoJumpBack=true&idtype=0&idcard=2****************6&createUserIdKeyByFlowKey=id&approverVerifyTypes=1&shortKey=yDwJ**cJKQWef"
    }
}
```

**Example 3: 获取某个流程合同的小程序跳转签署链接(隐藏某些按钮)**

1. 签署界面隐藏 更多操作按钮 和 查看详情按钮按钮 (Hides设置成[0,3])

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --FlowId yDwq7UU*Uu1vFD6uHSIyKQPf \
    --PathType 1 \
    --Name 典子谦 \
    --Mobile 13200000000 \
    --EndPoint APP \
    --AutoJumpBack True \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Hides 0 3
```

Output: 
```
{
    "Response": {
        "RequestId": "s1693791166610672060",
        "SchemeUrl": "pages/guide?from=default&where=mini&id=yDwq7UU*Uu1vFD6uHSIyKQPf&to=CONTRACT_DETAIL&name=%E5%91%&phone=MTkx**0OTc3NjA%3D&autoJumpBack=true&idtype=0&idcard=2****************6&createUserIdKeyByFlowKey=id&approverVerifyTypes=1&shortKey=yDwJ**cJKQWef"
    }
}
```

**Example 4: 获取某个流程合同的签署链接(主代子)**

1. 主企业代子企业创建小程序签署链接(Agent参数中的ProxyOrganizationId设置成子企业ID)
2. 签署链接是HTTP长链(EndPoint设置成HTTP，默认为此值)

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Agent.ProxyOrganizationId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --FlowId yDwq7UU*Uu1vFD6uHSIyKQPf \
    --PathType 1 \
    --EndPoint HTTP \
    --Name 典子谦 \
    --Mobile 13200000000
```

Output: 
```
{
    "Response": {
        "RequestId": "s1693829642597082849",
        "SchemeUrl": "https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?where=mini&from=SFY&id=yDwq7UU*Uu1vFD6uHSIyKQPf&to=MVP_CONTRACT_COVER&name=%E5**5%B2%A9&phone=M**c3NjA%3D&idtype=0&idcard=2****************6&createUserIdKeyByFlowKey=id&approverVerifyTypes=1&ignoreApproverSwitch=1&shortKey=yDwJCUemZ**A43"
    }
}
```

**Example 5: 错误的示例- 获取某个流程合同的小程序跳转签署链接，PathType值没有传对（应该传1- 小程序合同详情)**

1. 获取小程序跳转签署链接(EndPoint设置成APP)
2. 不指定跳转的页面类型(不传PathType或者传0值)

Input: 

```
tccli ess CreateSchemeUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwq7UU*Uu1vFD6uHSIyKQPf \
    --EndPoint APP \
    --Name 典子谦 \
    --Mobile 13200000000
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.NoSupportJumpPage",
            "Message": "APP类型不支持跳转到电子签主页或合同列表页"
        },
        "RequestId": "s1693830251815551087"
    }
}
```

