**Example 1: 使用计划绑定密钥**

	
使用计划绑定密钥

Input: 

```
tccli apigateway BindSecretIds --cli-unfold-argument  \
    --UsagePlanId usagePlan-quqxvett \
    --AccessKeyIds AKID***********************************************
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "fcc3e46c-931d-4c58-88e9-f3cfc2251769"
    }
}
```

