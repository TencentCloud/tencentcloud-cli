**Example 1: 添加渠道本企业静默签以及企业签署人**

添加渠道本企业静默签以及企业签署人

Input: 

```
tccli essbasic ChannelCreateDynamicFlowApprover --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 6*****************314 \
    --Agent.ProxyOrganizationOpenId channel-org_openId \
    --Agent.AppId channel-appId \
    --FillDynamicFlowList.0.FlowId dynamicFlowIds \
    --FillDynamicFlowList.0.FlowApprovers.0.OrganizationName 渠道子公司企业 \
    --FillDynamicFlowList.0.FlowApprovers.0.OrganizationOpenId channel-org_openId \
    --FillDynamicFlowList.0.FlowApprovers.0.OpenId 员工openId \
    --FillDynamicFlowList.0.FlowApprovers.0.ApproverType ENTERPRISESERVER \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FillDynamicFlowList.0.FlowApprovers.1.OrganizationName 渠道子公司企业 \
    --FillDynamicFlowList.0.FlowApprovers.1.OrganizationOpenId channel-org_openId \
    --FillDynamicFlowList.0.FlowApprovers.1.OpenId 员工openId \
    --FillDynamicFlowList.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentValue 
```

Output: 
```
{
    "Response": {
        "DynamicFlowResultList": [
            {
                "DynamicFlowApproverList": [
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61iUugjySLvo742CmF8",
                        "SignId": "yDCYrUUckp7wh61fUugjySLSpPqQKwDk"
                    },
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61eUugjySLEuY1q4EvS",
                        "SignId": "yDCYrUUckp7wh61xUugjySLvLvRTpIG6"
                    }
                ],
                "FlowId": "dynamicFlowId"
            }
        ],
        "RequestId": "s1735021464414022010"
    }
}
```

**Example 2: 添加自建应用企业签署人**

添加自建应用企业签署人

Input: 

```
tccli essbasic ChannelCreateDynamicFlowApprover --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 6*****************314 \
    --Agent.ProxyOrganizationOpenId channel-org_openId \
    --Agent.AppId channel-appId \
    --FillDynamicFlowList.0.FlowId dynamicFlowIds \
    --FillDynamicFlowList.0.FlowApprovers.0.NotChannelOrganization True \
    --FillDynamicFlowList.0.FlowApprovers.0.OrganizationName 渠道子公司企业 \
    --FillDynamicFlowList.0.FlowApprovers.0.ApproverType ORGANIZATION \
    --FillDynamicFlowList.0.FlowApprovers.0.Name 员工姓名 \
    --FillDynamicFlowList.0.FlowApprovers.0.Mobile 员工手机号 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FillDynamicFlowList.0.FlowApprovers.1.NotChannelOrganization True \
    --FillDynamicFlowList.0.FlowApprovers.1.OrganizationName 渠道子公司企业 \
    --FillDynamicFlowList.0.FlowApprovers.1.Name 员工姓名 \
    --FillDynamicFlowList.0.FlowApprovers.1.Mobile 员工手机号 \
    --FillDynamicFlowList.0.FlowApprovers.1.ApproverType ORGANIZATION \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentValue 
```

Output: 
```
{
    "Response": {
        "DynamicFlowResultList": [
            {
                "DynamicFlowApproverList": [
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61iUugjySLvo742CmF8",
                        "SignId": "yDCYrUUckp7wh61fUugjySLSpPqQKwDk"
                    },
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61eUugjySLEuY1q4EvS",
                        "SignId": "yDCYrUUckp7wh61xUugjySLvLvRTpIG6"
                    }
                ],
                "FlowId": "dynamicFlowId"
            }
        ],
        "RequestId": "s1735021464414022010"
    }
}
```

**Example 3: 添加渠道方企业签署人,渠道企业可领取签署人和个人签署人**

添加渠道方企业签署人,渠道企业可领取签署人和个人签署人

Input: 

```
tccli essbasic ChannelCreateDynamicFlowApprover --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 6*****************314 \
    --Agent.ProxyOrganizationOpenId channel-org_openId \
    --Agent.AppId channel-appId \
    --FillDynamicFlowList.0.FlowId dynamicFlowIds \
    --FillDynamicFlowList.0.FlowApprovers.0.OrganizationName 渠道子公司企业 \
    --FillDynamicFlowList.0.FlowApprovers.0.OrganizationOpenId channel-org_openId \
    --FillDynamicFlowList.0.FlowApprovers.0.OpenId 员工openId \
    --FillDynamicFlowList.0.FlowApprovers.0.ApproverType ENTERPRISESERVER \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.0.SignComponents.0.ComponentValue  \
    --FillDynamicFlowList.0.FlowApprovers.1.OrganizationName 渠道子公司企业 \
    --FillDynamicFlowList.0.FlowApprovers.1.OrganizationOpenId channel-org_openId \
    --FillDynamicFlowList.0.FlowApprovers.1.ApproverType ENTERPRISESERVER \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.1.SignComponents.0.ComponentValue  \
    --FillDynamicFlowList.0.FlowApprovers.2.Name 员工姓名 \
    --FillDynamicFlowList.0.FlowApprovers.2.Mobile 员工手机号 \
    --FillDynamicFlowList.0.FlowApprovers.2.ApproverType PERSON \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentPosY 260 \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentWidth 100 \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.FileIndex 0 \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentType SIGN_SEAL \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentPage 1 \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentPosX 260 \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentHeight 100 \
    --FillDynamicFlowList.0.FlowApprovers.2.SignComponents.0.ComponentValue 
```

Output: 
```
{
    "Response": {
        "DynamicFlowResultList": [
            {
                "DynamicFlowApproverList": [
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61iUugjySLvo742CmF8",
                        "SignId": "yDCYrUUckp7wh61fUugjySLSpPqQKwDk"
                    },
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61eUugjySLEuY1q4EvS",
                        "SignId": "yDCYrUUckp7wh61xUugjySLvLvRTpIG6"
                    },
                    {
                        "ApproverStatus": 2,
                        "RecipientId": "yDCYrUUckp7wh61eUugjySLEurtyhjgh",
                        "SignId": "yDCYrUUckp7wh61xUugjySLvLrtghkl7"
                    }
                ],
                "FlowId": "dynamicFlowId"
            }
        ],
        "RequestId": "s1735021464414022010"
    }
}
```

