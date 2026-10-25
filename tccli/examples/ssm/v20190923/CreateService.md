**Example 1: 开通 ssm 服务**



Input: 

```
tccli ssm CreateService --cli-unfold-argument  \
    --PayMode PostPay \
    --ClientToken 123344
```

Output: 
```
{
    "Response": {
        "OrderId": "20260918311023705882391",
        "ResourceId": "ssm_260210396",
        "RequestId": "444eec98-00e2-42a1-87fe-8304b7500aa9"
    }
}
```

