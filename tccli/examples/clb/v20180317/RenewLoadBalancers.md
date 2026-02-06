**Example 1: 包年包月实例续费**

包年包月实例续费

Input: 

```
tccli clb RenewLoadBalancers --cli-unfold-argument  \
    --LoadBalancerIds lb-xxxxxxxx \
    --LBChargePrepaid.Period 2 \
    --LBChargePrepaid.RenewFlag AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "5b1357ae-8c0b-40f2-9b37-ceea95929668",
        "DealName": "20250922514107782498591"
    }
}
```

