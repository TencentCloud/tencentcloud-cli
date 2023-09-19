**Example 1: 生成个人小程序批量签署链接**

按照合同发起时候填入的信息生成批量签署链接，并通过FlowIds参数对用户可以批签的合同进行限制

Input: 

```
tccli essbasic ChannelCreateBatchSignUrl --cli-unfold-argument  \
    --IdCardNumber 610000000000000000 \
    --IdCardType ID_CARD \
    --Name 小明 \
    --NotifyType SMS \
    --Mobile 1234567890 \
    --Agent.ProxyOperator.OpenId test_open_id \
    --Agent.ProxyOrganizationOpenId test_org_open_id \
    --Agent.AppId yDxbWUyKQ*******4zjEB8mxCcDjAyF \
    --FlowIds yDwFdUUckpsw******yQ0af8bHosXQtb yDR1AUUgygj******uO4zjE8gTG7xvgH
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1684899114,
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "SignUrl": "https://ess.url.cn/FuP**Swc",
        "MiniAppPath": "pages/guide/index?shortKey=FuP3**wc"
    }
}
```

**Example 2: 生成企业经办人小程序批量签署链接**

按照合同发起时候填入的信息生成企业经办人批量签署链接，并通过FlowIds参数对用户可以批签的合同进行限制

Input: 

```
tccli essbasic ChannelCreateBatchSignUrl --cli-unfold-argument  \
    --IdCardNumber 610000000000000000 \
    --IdCardType ID_CARD \
    --Name 小明 \
    --NotifyType SMS \
    --Mobile 1234567890 \
    --OrganizationName 典子谦示例企业 \
    --Agent.ProxyOperator.OpenId test_open_id \
    --Agent.ProxyOrganizationOpenId test_org_open_id \
    --Agent.AppId yDxbWUyKQ*******4zjEB8mxCcDjAyF \
    --FlowIds yDwFdUUckpsw******yQ0af8bHosXQtb yDR1AUUgygj******uO4zjE8gTG7xvgH
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1684899114,
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "SignUrl": "https://ess.url.cn/FuP**Swc",
        "MiniAppPath": "pages/guide/index?shortKey=FuP3**wc"
    }
}
```

