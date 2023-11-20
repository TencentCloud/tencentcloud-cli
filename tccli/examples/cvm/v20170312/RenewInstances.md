**Example 1: 续费实例**

本示例用于续费一个实例，指定续费实例Id是ins-r8hr2upy，续费一个月，到期时通知过期但不自动续费。

Input: 

```
tccli cvm RenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

