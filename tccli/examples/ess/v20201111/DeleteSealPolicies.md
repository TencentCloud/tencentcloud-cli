**Example 1: 撤销印章授权**

撤销指定印章授权

Input: 

```
tccli ess DeleteSealPolicies --cli-unfold-argument  \
    --Operator.Channel string \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.OpenId 321654 \
    --Operator.ProxyIp 2.2.2.2 \
    --Operator.UserId 11234567890123456789012345678901 \
    --PolicyIds string
```

Output: 
```
{
    "Response": {
        "RequestId": "test"
    }
}
```

