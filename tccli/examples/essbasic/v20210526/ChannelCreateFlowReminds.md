**Example 1: 合同催办**

因为yDSL5UUckpokxl92UvwoHnSHf4RPOgu5我已经催办过, 所以返回"签署人 张三: 此签署人已催办过；", 对方不会在收到催办短信
yDSL5UUckpok9bd0UvwoHnxmejhdsSKL和yDSL5UUckpok4vmvUu7BBPOShktz8qHN催办成功, 对方收到短信

Input: 

```
tccli essbasic ChannelCreateFlowReminds --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDSL5UUckpok9bd0UvwoHnxmejhdsSKL yDSL5UUckpokxl92UvwoHnSHf4RPOgu5 yDSL5UUckpok4vmvUu7BBPOShktz8qHN
```

Output: 
```
{
    "Response": {
        "RemindFlowRecords": [
            {
                "CanRemind": true,
                "FlowId": "yDSL5UUckpok9bd0UvwoHnxmejhdsSKL",
                "RemindMessage": "签署人 王五: 催办成功；"
            },
            {
                "CanRemind": true,
                "FlowId": "yDSL5UUckpokxl92UvwoHnSHf4RPOgu5",
                "RemindMessage": "签署人 张三: 此签署人已催办过；"
            },
            {
                "CanRemind": true,
                "FlowId": "yDSL5UUckpok4vmvUu7BBPOShktz8qHN",
                "RemindMessage": "签署人 张三: 催办成功；签署人 李四: 催办成功；"
            }
        ],
        "RequestId": "4ad2f917-5c8e-4071-bae7-caa43387d0c3"
    }
}
```

