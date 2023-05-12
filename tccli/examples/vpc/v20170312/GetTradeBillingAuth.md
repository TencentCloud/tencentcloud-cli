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
            "Version": "abc",
            "SecretId": "abc",
            "Timestamp": 1,
            "Signature": "abc",
            "Nonce": "abc"
        },
        "RequestId": "abc"
    }
}
```

