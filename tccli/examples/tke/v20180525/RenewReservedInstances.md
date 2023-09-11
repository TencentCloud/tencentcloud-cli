**Example 1: 续费预留券实例**

续费结果请调用查询接口检验。

Input: 

```
tccli tke RenewReservedInstances --cli-unfold-argument  \
    --ReservedInstanceIds eksri-103ypth4 eksri-mloz4700 \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag DISABLE_NOTIFY_AND_MANUAL_RENEW \
    --ClientToken renew-unique-token
```

Output: 
```
{
    "Response": {
        "RequestId": "cabe1292-b7f9-43bc-aeac-f50e59521be1"
    }
}
```

