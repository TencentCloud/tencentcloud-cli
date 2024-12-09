**Example 1: 预付费下单屏蔽余额支付场景-获取AUTH**

预付费下单屏蔽余额支付场景-获取AUTH

Input: 

```
tccli vpc GetTradeBillingAuth --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Auth": {
            "Version": "ver1",
            "SecretId": "sxuwq1Kx123xz",
            "Timestamp": 1,
            "Signature": "123xz1a",
            "Nonce": "17406"
        },
        "RequestId": "abc"
    }
}
```

