**Example 1: 查询**



Input: 

```
tccli cngw DescribeAIGWLLMModelAPIIPRestriction --cli-unfold-argument  \
    --GatewayId gateway-bb346e76 \
    --ModelAPIId 7e01bc3d338148728ab02e9b854b911e
```

Output: 
```
{
    "Response": {
        "Result": {
            "AddressList": [
                "127.0.0.1/8"
            ],
            "Enable": true,
            "RestrictionType": "whiteList"
        },
        "RequestId": "5effbd06-bff2-42af-8776-9e4c51bba866"
    }
}
```

