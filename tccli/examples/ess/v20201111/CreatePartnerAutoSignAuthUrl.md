**Example 1: 创建他方自动签授权链接-我方授权**

创建他方自动签授权链接（AuthToMe设置成false）


Input: 

```
tccli ess CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --AuthorizedOrganizationId yDRt2UUgygqxuvlqUuO4zjEySqVWqO9J \
    --AuthToMe False \
    --SealTypes OFFICIAL
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1721984586,
        "MiniAppPath": "/pages/guide/index?shortKey=yDCpEUNqf8CyuealGCfc",
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 ",
        "Url": "https://essurl.cn/g4sjUBHlHx"
    }
}
```

**Example 2: 创建他方自动签授权链接-他方授权**

他方授权给我方（AuthToMe被设置成true）

Input: 

```
tccli ess CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --AuthorizedOrganizationName 他方企业名称 \
    --AuthToMe True \
    --SealTypes OFFICIAL
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1721984586,
        "MiniAppPath": "/pages/guide/index?shortKey=yDCpEUNqf8CyuealGCfc",
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 ",
        "Url": "https://essurl.cn/g4sjUBHlHx"
    }
}
```

