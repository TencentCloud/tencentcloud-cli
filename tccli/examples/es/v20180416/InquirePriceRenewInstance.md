**Example 1: ES集群实例续费询价**

ES集群实例续费询价

Input: 

```
tccli es InquirePriceRenewInstance --cli-unfold-argument  \
    --InstanceId es_xdfds
```

Output: 
```
{
    "Response": {
        "Discount": 65,
        "OriginalPrice": 1.15,
        "DiscountPrice": 0.75,
        "Currency": "CNY",
        "RequestId": "027e29ad-f2b5-4929-b479-96bf541df7e7"
    }
}
```

