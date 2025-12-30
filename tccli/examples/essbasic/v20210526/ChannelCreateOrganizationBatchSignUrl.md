**Example 1: 创建合同组签署链接**



Input: 

```
tccli essbasic ChannelCreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Agent.AppId 60exxxxxxxxxxxxxxxxxxxxxc16e9 \
    --Agent.ProxyOrganizationOpenId org_open_id \
    --Name  \
    --Mobile  \
    --FlowGroupId yDxxxxxxxxxxxxxxxxxxxxxxxx \
    --OpenId user_open_id
```

Output: 
```
{
    "Response": {
        "SignUrl": "https://embed.test.qian.tencent.cn/console/?channel=PROXYCHANNEL&expiredTime=1695805069&code=xxxxx&menuStatus=ENABLE&token=xxxx",
        "ExpiredTime": 0,
        "RequestId": "s1695804769054178191"
    }
}
```

**Example 2: 创建签署链接**

待签署的合同

Input: 

```
tccli essbasic ChannelCreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Agent.AppId 60exxxxxxxxxxxxxxxxxxxxxc16e9 \
    --Agent.ProxyOrganizationOpenId org_open_id \
    --Name  \
    --Mobile  \
    --FlowIds yDxxxxxxxxxxxxxxxxxxxxxxxx \
    --OpenId user_open_id
```

Output: 
```
{
    "Response": {
        "SignUrl": "https://embed.test.qian.tencent.cn/console/?channel=PROXYCHANNEL&expiredTime=1695805069&code=xxxxx&menuStatus=ENABLE&token=xxxx",
        "ExpiredTime": 0,
        "RequestId": "s1695804769054178191"
    }
}
```

**Example 3: 创建企业动态签署领取链接**

发起合同指定B端企业员工为动态签署方，通过此接口获取动态领取链接。

Input: 

```
tccli essbasic ChannelCreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.ProxyOperator.OpenId kevinlcheng \
    --FlowIds yDtK2UUckpfmgingU1UyHCZxCSSvzgqj \
    --CanBatchReject True \
    --RecipientIds yDtK2UUckpfmgindUyHCZxCEZrJgOW8c
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1767619219,
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-batchsign?embed=1&expiredOn=1767619219&code=yDtK2UUckpfmg5e1UyDuCxQBXaYPsgdA&shortKey=yDtK2UemxuuTcRfVpk7b&channel=PROXYCHANNEL",
        "RequestId": "1e564965-8e7c-4a3e-bc8c-c35be86937ad"
    }
}
```

**Example 4: 创建企业动态签署领取链接，并且预设企业OpenId**

发起合同指定B端企业员工为动态签署方，通过此接口获取动态领取链接。

1.预设企业OpenId，要求只能由对应企业员工点击领取链接进行领取
2.指定要求全部合同领取进行签署。

Input: 

```
tccli essbasic ChannelCreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.ProxyOperator.OpenId kevinlcheng \
    --FlowIds yDtK2UUckpfmgingU1UyHCZxCSSvzgqj \
    --RecipientIds yDtK2UUckpfmgindUyHCZxCEZrJgOW8c \
    --DynamicSignOption.DynamicReceiveType 1 \
    --DynamicSignOption.OrganizationOpenId dian_zi_qian \
    --CanBatchReject True
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1767619145,
        "SignUrl": "https://embed.test.qian.tencent.cn/contract-batchsign?embed=1&expiredOn=1767619145&code=yDtK2UUckpfmpuhxUuyfSWJxqnEnA7KP&shortKey=yDtK2UemxQpCrgNgy100&channel=PROXYCHANNEL",
        "RequestId": "b9f75514-0559-4699-be54-11019de12574"
    }
}
```

