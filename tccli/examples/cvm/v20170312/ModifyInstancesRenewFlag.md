**Example 1: 修改两个实例的续费标识**

本示例用于修改两个实例的续费标识。

Input: 

```
tccli cvm ModifyInstancesRenewFlag --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

