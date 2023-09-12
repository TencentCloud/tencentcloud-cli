**Example 1: UserId和 姓名手机都传递，生成的链接基于UserId生成**

UserId和 姓名手机都传递，生成的链接基于UserId生成

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s yDwFmUUckpstqfvzUxxx3jo1f3cqjkGm yDwFmUUckpst10i3UxxxSat8PWOt2iQF \
    --UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Name 张三 \
    --Mobile 18888888888
```

Output: 
```
{
    "Response": {
        "SignUrl": "abc",
        "ExpiredTime": 0,
        "RequestId": "abc"
    }
}
```

**Example 2: 参与人不在链接中， 无法生成链接报错**

参与人不在链接中， 无法生成链接报错

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s yDwFmUUckpstqfvzUxxx3jo1f3cqjkGm yDwFmUUckpst10i3UxxxSat8PWOt2iQF \
    --Name 典子谦 \
    --Mobile 13200000000
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "[yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s yDwFmUUckpstqfvzUxxx3jo1f3cqjkGm yDwFmUUckpst10i3UxxxSat8PWOt2iQF]，经办人不是合同的实际签署人;"
        },
        "RequestId": "xxxxxxxxxxxxxxx"
    }
}
```

**Example 3: 根据员工UserId获取批量签署链接**

根据员工UserId获取批量签署链接

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s yDwFmUUckpstqfvzUxxx3jo1f3cqjkGm yDwFmUUckpst10i3UxxxSat8PWOt2iQF \
    --UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj
```

Output: 
```
{
    "Response": {
        "SignUrl": "https://qian.tencent.com/xxxxxx?xxxx=xxx",
        "ExpiredTime": 1685011753,
        "RequestId": "xxxxxxxxxxxxxxx"
    }
}
```

**Example 4: 根据员工姓名和手机号获取批量签署链接**

根据员工姓名和手机号获取批量签署链接

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s yDwFmUUckpstqfvzUxxx3jo1f3cqjkGm yDwFmUUckpst10i3UxxxSat8PWOt2iQF \
    --Name 典子谦 \
    --Mobile 13200000000
```

Output: 
```
{
    "Response": {
        "SignUrl": "https://qian.tencent.com/xxxxxx?xxxx=xxx",
        "ExpiredTime": 1685011753,
        "RequestId": "xxxxxxxxxxxxxxx"
    }
}
```

