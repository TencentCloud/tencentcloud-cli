**Example 1: 预释放出价**



Input: 

```
tccli domain BiddingPreRelease --cli-unfold-argument  \
    --BusinessId abc \
    --Price 0
```

Output: 
```
{
    "Response": {
        "IsNeedPay": true,
        "BillingParam": "abc",
        "RequestId": "abc"
    }
}
```

