**Example 1: 续费企业版预付费实例**



Input: 

```
tccli tcr RenewInstance --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --RegistryChargePrepaid.Period 1 \
    --RegistryChargePrepaid.RenewFlag 1 \
    --Flag 0
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-12345",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

