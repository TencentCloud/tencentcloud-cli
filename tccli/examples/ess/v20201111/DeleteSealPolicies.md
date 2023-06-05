**Example 1: 撤销印章授权**

撤销指定印章授权

Input: 

```
tccli ess DeleteSealPolicies --cli-unfold-argument  \
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

