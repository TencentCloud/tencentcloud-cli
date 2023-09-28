**Example 1: 创建通用型预留券**

创建的预留券是地域抵扣范围，如需修改抵扣范围，请调用修改抵扣范围接口。

Input: 

```
tccli tke CreateReservedInstances --cli-unfold-argument  \
    --ReservedInstanceSpec.Type common \
    --ReservedInstanceSpec.Cpu 1 \
    --ReservedInstanceSpec.Memory 2 \
    --InstanceCount 1 \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --ClientToken my-unique-token
```

Output: 
```
{
    "Response": {
        "RequestId": "adbb030e-163e-44c6-a940-fb42190d0d56",
        "ReservedInstanceIds": [
            "eksri-mloz4700"
        ]
    }
}
```

