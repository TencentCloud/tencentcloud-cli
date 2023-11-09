**Example 1: 领取合同成功**

领取2个未归属的合同给当前员工

Input: 

```
tccli essbasic ChannelCreateBoundFlows --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDSLZUUckpotp24bUER7iHn1TnyrRvG5 yDSLZUUckpotplq0UELP595SOtvY2jPa
```

Output: 
```
{
    "Response": {
        "RequestId": "3a00c125-b7fd-4dcb-879c-651bd471ac15"
    }
}
```

**Example 2: 领取失败**

有一个合同无法被领取就会导致所有的合同无法领取, 例子中的yDSLZUUckpotplq0UELP595SOtvY2jPa已经领取导致请求失败

Input: 

```
tccli essbasic ChannelCreateBoundFlows --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDSLZUUckpotp24bUER7iHn1TnyrRvG5 yDSLZUUckpotplq0UELP595SOtvY2jPa
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "此签署流程状态无法领取"
        },
        "RequestId": "0f61a7b2-a02d-44b8-9a05-66cd0cbc0d37"
    }
}
```

