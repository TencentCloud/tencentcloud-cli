**Example 1: 续费环境**

给环境续费1个月，并自动使用代金券抵扣。
续费是异步操作，下单之后，可以通过DescribeBillingInfo接口查询最新的到期时间。

Input: 

```
tccli tcb RenewEnv --cli-unfold-argument  \
    --EnvId cloudbase-8grqda2hfc2f62bb \
    --Period 1 \
    --AutoVoucher True
```

Output: 
```
{
    "Response": {
        "RequestId": "8a235158-b278-41ee-b3c5-0f4c39797e5c"
    }
}
```

