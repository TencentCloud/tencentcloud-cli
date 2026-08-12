**Example 1: 设置 clawpro 实例续费标记**



Input: 

```
tccli smh SetClawProSpaceRenewFlagInternal --cli-unfold-argument  \
    --LibraryId smh314r4e77fgfl3 \
    --InstanceId s2vkfExGzT002 \
    --RenewFlag MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "InstanceId": "s2vkfExGzT002",
        "RenewFlag": "MANUAL_RENEW",
        "SpaceId": "space3vnsam2g0c2ff",
        "RequestId": "178cf44e-a878-4d82-859a-77a1c3da4f3a"
    }
}
```

