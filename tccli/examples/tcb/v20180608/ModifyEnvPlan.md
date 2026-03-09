**Example 1: 云开发环境套餐变更为标准版**

将云开发环境变更为标准版，并自动使用代金券抵扣。
变配是异步操作，下单成功后，可以通过DescribeBillingInfo接口查到当前环境的套餐是否已生效。

Input: 

```
tccli tcb ModifyEnvPlan --cli-unfold-argument  \
    --EnvId cloudbase-8grqda2hfc2f62bb \
    --PackageId baas_pf_standard \
    --AutoVoucher True
```

Output: 
```
{
    "Response": {
        "RequestId": "4caf24c6-3cb8-438a-ae46-cfa75694224a"
    }
}
```

