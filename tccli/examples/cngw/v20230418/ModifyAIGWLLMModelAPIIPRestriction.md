**Example 1: 修改**



Input: 

```
tccli cngw ModifyAIGWLLMModelAPIIPRestriction --cli-unfold-argument  \
    --GatewayId gateway-bb346e76 \
    --ModelAPIId 7e01bc3d338148728ab02e9b854b911e \
    --Enable True \
    --RestrictionType whiteList \
    --AddressList 127.0.0.1/8
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "d347cd02-0b53-49e9-ac98-6137f5c8dbb2"
    }
}
```

