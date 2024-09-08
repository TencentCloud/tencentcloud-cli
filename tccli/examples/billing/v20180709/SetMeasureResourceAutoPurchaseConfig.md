**Example 1: 鉴权失败**

鉴权失败

Input: 

```
tccli billing SetMeasureResourceAutoPurchaseConfig --cli-unfold-argument  \
    --ProductCode p_trade_t_s \
    --ResourceId asdd \
    --AutoRePurchaseFlag 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "ce128220-2337-4c74-bc6f-ac6344762d23"
    }
}
```

**Example 2: 设置自动新购**



Input: 

```
tccli billing SetMeasureResourceAutoPurchaseConfig --cli-unfold-argument  \
    --ProductCode p_rav \
    --ResourceId 100052301 \
    --AutoRePurchaseFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "95577512-8a64-4f38-a770-45d3a8bd6be7"
    }
}
```

