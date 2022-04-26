**Example 1: 续费实例**



Input: 

```
tccli lighthouse RenewInstances --cli-unfold-argument  \
    --InstanceIds lhins-1cte6j63 lhins-oxfq8tad \
    --InstanceChargePrepaid.Period 1 \
    --AutoVoucher True \
    --RenewDataDisk True
```

Output: 
```
{
    "Response": {
        "RequestId": "c139e106-cdb2-4923-8f1e-ea1dc4fe3a47"
    }
}
```

