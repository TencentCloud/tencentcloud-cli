**Example 1: 创建他方自动签授权链接**

创建他方自动签授权链接


Input: 

```
tccli ess CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Operator.UserId yDSxxxxxxxxxOnHtH51 \
    --AuthorizedOrganizationId yDRt2UUgygqxuvlqUuO4zjEySqVWqO9J \
    --SealTypes OFFICIAL
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1721984586,
        "MiniAppPath": "/pages/guide/index?shortKey=yDCpEUNqf8CyuealGCfc",
        "RequestId": "s1721379786690441960",
        "Url": "https://test.essurl.cn/g4sjUBHlHx"
    }
}
```

