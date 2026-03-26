**Example 1: 创建LightHouse实例**

创建LightHouse实例

Input: 

```
tccli tcb CreateVmInstance --cli-unfold-argument  \
    --EnvId free2-2gi6dzbde85f86a0 \
    --Type LightHouse \
    --LightHouseBundleId bundle_rs_mc_med1_02 \
    --LightHouseBlueprintId lhbp-3qjk6slu \
    --InstanceName my new lighthouse instance
```

Output: 
```
{
    "Response": {
        "RequestId": "f12f533b-bc0a-403a-97a5-0a5cb9299d25"
    }
}
```

