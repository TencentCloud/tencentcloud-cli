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

**Example 3: 合同发起的时候签署方信息和生成链接中的不一致**

合同（yDR1AUUgygja******uO4zjEB8zAkJEFN）中的参与方为：【姓名：张三 ，手机号：18888888888】，发起的时候并未填入证件号且18888888888手机号并未在腾讯电子签注册实名。 

此时，如果使用 【姓名：张三，手机号：17777777777】生成批量签署链接，且FlowIds参数传入（yDR1AUUgygja******uO4zjEB8zAkJEFN）时，会报错，提示签署方信息不存在。

因为手机号不同，无法定位到签署方。 此时，除了将手机号修改成 18888888888 之外来解决问题，也可以在发起合同和生成链接的时候传入证件信息，保证姓名和证件一致的情况下，手机号可以不相同。

Input: 

```
tccli essbasic ChannelCreateBatchSignUrl --cli-unfold-argument  \
    --IdCardNumber  \
    --IdCardType  \
    --Name 张三 \
    --NotifyType SMS \
    --Mobile 17777777777 \
    --Agent.ProxyOperator.OpenId test_open_id \
    --Agent.ProxyOrganizationOpenId test_org_open_id \
    --Agent.AppId yDxbWUyKQ*******4zjEB8mxCcDjAyF \
    --FlowIds yDR1AUUgygja******uO4zjEB8zAkJEFN
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "合同[yDR1AUUgygja******uO4zjEB8zAkJEFN]不包含链接中的参与方信息, 请确保链接姓名手机号等信息与合同中一致"
        },
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

**Example 4: 生成动态签署人批量领取链接**

按照合同发起时候返回的合同信息生成批量签署链接，通过FlowIds参数对用户可以批签的合同进行限制，并指定批量领取的动态签署方。

Input: 

```
tccli essbasic ChannelCreateBatchSignUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId test_open_id \
    --Agent.ProxyOrganizationOpenId test_org_open_id \
    --Agent.AppId yDxbWUyKQ*******4zjEB8mxCcDjAyF \
    --FlowIds yDwFdUUckpsw******yQ0af8bHosXQtb yDR1AUUgygj******uO4zjE8gTG7xvgH \
    --FlowBatchUrlInfo.FlowBatchApproverInfos.0.FlowId yDC5yUUckpwexoz4UuoHfkT1DMEDQSG5 \
    --FlowBatchUrlInfo.FlowBatchApproverInfos.0.RecipientId yDC5yUUckpwexozwUuoHfkTwB00zdfLo
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

