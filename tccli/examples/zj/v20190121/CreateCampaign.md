**Example 1: CreateCampaign**



Input: 

```
tccli zj CreateCampaign --cli-unfold-argument  \
    --License KA3431QZPU \
    --SendTime 1578977657 \
    --Name paas \
    --Strategies.0.CrowdID 192 \
    --Strategies.0.Items.0.Id 1486 \
    --Strategies.0.Items.0.ContentType 1 \
    --Strategies.0.Items.1.Id 569943 \
    --Strategies.0.Items.1.ContentType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CampaignId": 47
        },
        "RequestId": "111111"
    }
}
```

