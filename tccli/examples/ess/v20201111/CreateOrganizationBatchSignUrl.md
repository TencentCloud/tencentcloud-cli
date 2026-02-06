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
        "ExpiredTime": 1706100107,
        "RequestId": "s1705495307288609862",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100107&code=yDCNBUUckpvlibz6UEMbkWeSzl6YurH0&shortKey=yDCNBUzgvS93aBhXs3ae&channel=TENCENTCLOUD"
    }
}
```

**Example 2: 创建企业用户动态领取链接**

发起流程后，给其中的B端动态签署方创建领取链接。

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDC5yUUntf6vnnUxxBTyJ8Ps0WGqAuHL yDC5yUUntf6fccUEgcyeHwPz4wjnDSI4 \
    --RecipientIds yDC5yUUntf6vn0UxxBTyJvfv3Xlckcye yDC5yUUntf6mdgUEgcyeHCpCDmDjbsQJ
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1706100107,
        "RequestId": "s1705495307288609862",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100107&code=yDCNBUUckpvlibz6UEMbkWeSzl6YurH0&shortKey=yDCNBUzgvS93aBhXs3ae&channel=TENCENTCLOUD"
    }
}
```

**Example 3: 创建企业用户动态领取链接，并且预设企业名称**

发起流程后，给其中的B端动态签署方创建领取链接，并且预设企业名称。

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDC5yUUntf6vnnUxxBTyJ8Ps0WGqAuHL yDC5yUUntf6fccUEgcyeHwPz4wjnDSI4 \
    --RecipientIds yDC5yUUntf6vn0UxxBTyJvfv3Xlckcye yDC5yUUntf6mdgUEgcyeHCpCDmDjbsQJ \
    --DynamicSignOption.OrganizationName 典子谦有限公司
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1706100107,
        "RequestId": "s1705495307288609862",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100107&code=yDCNBUUckpvlibz6UEMbkWeSzl6YurH0&shortKey=yDCNBUzgvS93aBhXs3ae&channel=TENCENTCLOUD"
    }
}
```

**Example 4: 参与人不在链接中， 无法生成链接报错**

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

**Example 5: 基于RecipientIds 生成他方签署链接**



Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --UserId  \
    --Name  \
    --Mobile  \
    --FlowIds yDC5yUUntf6vnnUxxBTyJ8Ps0WGqAuHL yDC5yUUntf6fccUEgcyeHwPz4wjnDSI4 \
    --RecipientIds yDC5yUUntf6vn0UxxBTyJvfv3Xlckcye yDC5yUUntf6mdgUEgcyeHCpCDmDjbsQJ
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1706100107,
        "RequestId": "s1705495307288609862",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100107&code=yDCNBUUckpvlibz6UEMbkWeSzl6YurH0&shortKey=yDCNBUzgvS93aBhXs3ae&channel=TENCENTCLOUD"
    }
}
```

**Example 6: 根据员工UserId获取批量签署链接**

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
        "ExpiredTime": 1706100167,
        "RequestId": "s1705495367413358264",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100167&code=yDCNBUUckpvliyc7UxKACG8SaaySZ0Cq&shortKey=yDCNBUzgv1JtyCflmM2f&channel=TENCENTCLOUD"
    }
}
```

**Example 7: 根据员工姓名和手机号获取批量签署链接**

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
        "ExpiredTime": 1706100228,
        "RequestId": "s1705495428038618994",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100228&code=yDCNBUUckpvlibzeUEMbkWeRNyTH5WNK&shortKey=yDCNBUzgvw1blVbE1L7c&channel=TENCENTCLOUD"
    }
}
```

**Example 8: 获取合同组签署链接**



Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowGroupId yDwFmUUckpstqfvzUxxx3jo1f3cqjkGm \
    --UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Name 张三 \
    --Mobile 18888888888
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1706100107,
        "RequestId": "s1705495307288609862",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100107&code=yDCNBUUckpvlibz6UEMbkWeSzl6YurH0&shortKey=yDCNBUzgvS93aBhXs3ae&channel=TENCENTCLOUD"
    }
}
```

**Example 9: 创建企业用户动态领取链接，指定要求全部领取签署**

发起流程后，给其中的B端动态签署方创建领取链接，并且要求必须全部领取签署。

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UXXXzjEwg0vjoimj \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDC5yUUntf6vnnUxxBTyJ8Ps0WGqAuHL yDC5yUUntf6fccUEgcyeHwPz4wjnDSI4 \
    --RecipientIds yDC5yUUntf6vn0UxxBTyJvfv3Xlckcye yDC5yUUntf6mdgUEgcyeHCpCDmDjbsQJ \
    --DynamicSignOption.DynamicReceiveType 1
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1706100107,
        "RequestId": "s1705495307288609862",
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-sign?embed=1&expiredOn=1706100107&code=yDCNBUUckpvlibz6UEMbkWeSzl6YurH0&shortKey=yDCNBUzgvS93aBhXs3ae&channel=TENCENTCLOUD"
    }
}
```

