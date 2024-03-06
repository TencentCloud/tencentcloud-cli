**Example 1: 创建个人用户H5签署链接**

发起流程后，给其中的C端签署人创建签署链接

Input: 

```
tccli essbasic ChannelCreateFlowSignUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --FlowApproverInfos.0.Mobile 13200000000 \
    --FlowApproverInfos.0.Name 典子谦 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverType": "PERSON",
                "LongUrl": "https://quick.qian.tencent.cn/home?ApproverIdCardNumber=NCoqK***&ApproverIdCardType=ID_CARD&ApproverMobile=MTU4%3D&ApproverName=%25E9%2583%2591%****1%2589&ApproverType=1&Code=yDwhGUUckp3s****z1m3P&CodeType=QUICK&FlowId=yD****T&ShowHeader=1&token=HXC***d",
                "Mobile": "13200000000",
                "Name": "典子谦",
                "SignUrl": "https://test.essurl.cn/HXC***d"
            }
        ],
        "RequestId": "s1690514917653165172"
    }
}
```

**Example 2: 创建企业用户H5签署链接**

发起流程后，给其中的B端签署人创建签署链接

Input: 

```
tccli essbasic ChannelCreateFlowSignUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --FlowApproverInfos.0.ApproverType ORGANIZATION \
    --FlowApproverInfos.0.OrganizationOpenId org_dianziqian \
    --FlowApproverInfos.0.OpenId n9527 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverType": "ORGANIZATION",
                "LongUrl": "https://quick.qian.tencent.cn/home?ApproverIdCardNumber=NCoqK***&ApproverIdCardType=ID_CARD&ApproverMobile=MTU4%3D&ApproverName=%25E9%2583%2591%****1%2589&ApproverType=0&Code=yDwhGUUckp3s****z1m3P&CodeType=QUICK&FlowId=yD****T&ShowHeader=1&token=HXC***d",
                "Mobile": "13200000000",
                "Name": "典子谦",
                "SignUrl": "https://test.essurl.cn/HXC***d"
            }
        ],
        "RequestId": "s1690514917653165172"
    }
}
```

**Example 3: 创建企业用户H5预览链接**

发起流程后，给其中的B端签署人创建预览链接

Input: 

```
tccli essbasic ChannelCreateFlowSignUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --FlowApproverInfos.0.ApproverType ORGANIZATION \
    --FlowApproverInfos.0.OrganizationOpenId org_dianziqian \
    --FlowApproverInfos.0.OpenId n9527 \
    --UrlType 1 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverType": "ORGANIZATION",
                "LongUrl": "https://quick.qian.tencent.cn/home?ApproverIdCardNumber=NCoqK***&ApproverIdCardType=ID_CARD&ApproverMobile=MTU4%3D&ApproverName=%25E9%2583%2591%****1%2589&PreviewType=2&Code=yDwhGUUckp3s****z1m3P&CodeType=QUICK&FlowId=yD****T&ShowHeader=1&token=HXC***d",
                "Mobile": "13200000000",
                "Name": "典子谦",
                "SignUrl": "https://test.essurl.cn/HXC***d"
            }
        ],
        "RequestId": "s1690514917653165172"
    }
}
```

**Example 4: 创建合同发起方预览链接**

发起流程后，给其中的合同发起方创建预览链接

Input: 

```
tccli essbasic ChannelCreateFlowSignUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --UrlType 1 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverType": "",
                "LongUrl": "https://quick.qian.tencent.cn/home?ApproverIdCardNumber=NCoqK***&ApproverIdCardType=ID_CARD&ApproverMobile=MTU4%3D&ApproverName=%25E9%2583%2591%****1%2589&PreviewType=2&Code=yDwhGUUckp3s****z1m3P&CodeType=QUICK&FlowId=yD****T&ShowHeader=1&token=HXC***d",
                "Mobile": "",
                "Name": "",
                "SignUrl": "https://test.essurl.cn/HXC***d"
            }
        ],
        "RequestId": "s1690514917653165172"
    }
}
```

**Example 5: 创建个人用户H5签署链接，并指定视频问答模式认证**

发起流程后，给其中的C端签署人创建签署链接，并指定视频问答模式认证

Input: 

```
tccli essbasic ChannelCreateFlowSignUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --FlowApproverInfos.0.Mobile 13200000000 \
    --FlowApproverInfos.0.Name 典子谦 \
    --FlowApproverInfos.0.ApproverSignTypes 1 \
    --FlowApproverInfos.0.Intention.IntentionType 1 \
    --FlowApproverInfos.0.Intention.IntentionQuestions.0.Question 请问，您是否同意签署本协议？可语音回复“同意”或“不同意”。 \
    --FlowApproverInfos.0.Intention.IntentionQuestions.0.Answers 同意 我同意 \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm
```

Output: 
```
{
    "Response": {
        "FlowApproverUrlInfos": [
            {
                "ApproverType": "PERSON",
                "LongUrl": "https://quick.qian.tencent.cn/home?ApproverIdCardNumber=NCoqK***&ApproverIdCardType=ID_CARD&ApproverMobile=MTU4%3D&ApproverName=%25E9%2583%2591%****1%2589&ApproverType=1&Code=yDwhGUUckp3s****z1m3P&CodeType=QUICK&FlowId=yD****T&ShowHeader=1&token=HXC***d",
                "Mobile": "13200000000",
                "Name": "典子谦",
                "SignUrl": "https://test.essurl.cn/HXC***d"
            }
        ],
        "RequestId": "s1690514917653165172"
    }
}
```

