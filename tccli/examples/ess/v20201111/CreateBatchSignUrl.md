**Example 1: 生成个人小程序批量签署链接**

按照合同发起时候填入的信息生成批量签署链接，并通过FlowIds参数对用户可以批签的合同进行限制

Input: 

```
tccli ess CreateBatchSignUrl --cli-unfold-argument  \
    --IdCardNumber 620000198802020000 \
    --IdCardType ID_CARD \
    --Name 典子谦 \
    --NotifyType SMS \
    --Mobile 13200000000 \
    --Operator.UserId yDRCLUUgygq2******uO4zjEwg0vjoimj \
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
tccli ess CreateBatchSignUrl --cli-unfold-argument  \
    --IdCardNumber 620000198802020000 \
    --IdCardType ID_CARD \
    --Name 典子谦 \
    --NotifyType SMS \
    --Mobile 13200000000 \
    --OrganizationName 典子谦示例企业 \
    --Operator.UserId yDRCLUUgygq2******uO4zjEwg0vjoimj \
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

