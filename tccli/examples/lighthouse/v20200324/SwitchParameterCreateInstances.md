**Example 1: 新购参数转换-成功返回**

新购参数转换-成功返回

Input: 

```
tccli lighthouse SwitchParameterCreateInstances --cli-unfold-argument  \
    --BlueprintId bp-11110001 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceName Ubuntu \
    --BundleId bundle_ntp_small1_500
```

Output: 
```
{
    "Response": {
        "InstanceOrder": "",
        "RequestId": "bf9c621a-8414-4797-beae-efe1fba90fe9"
    }
}
```

