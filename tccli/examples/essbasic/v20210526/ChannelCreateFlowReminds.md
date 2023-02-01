**Example 1: 电子签渠道版-合同催办接口**



Input: 

```
tccli essbasic ChannelCreateFlowReminds --cli-unfold-argument  \
    --Agent.ProxyAppId c17bdf***********200fef3d \
    --Agent.ProxyOperator.OpenId 00498cc***********3aff766cac \
    --Agent.AppId xx \
    --Agent.ProxyOrganizationOpenId d7c13a8***********0ee248f04 \
    --FlowIds xxx
```

Output: 
```
{
    "Response": {
        "RemindFlowRecords": [
            {
                "CanRemind": true,
                "FlowId": "xxx",
                "RemindMessage": "签署人 xxx: 此签署人已催办过；"
            }
        ],
        "RequestId": "s1675065415484184252"
    }
}
```

