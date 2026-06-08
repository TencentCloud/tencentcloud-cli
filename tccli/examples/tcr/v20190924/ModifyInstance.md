**Example 1: 更新实例信息**

调整实例规格

Input: 

```
tccli tcr ModifyInstance --cli-unfold-argument  \
    --RegistryId tcr-abc123 \
    --RegistryType premium
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

**Example 2: 更新实例**

调整是否开启多版本控制

Input: 

```
tccli tcr ModifyInstance --cli-unfold-argument  \
    --RegistryId tcr-268s8hmm \
    --EnableCosVersioning False
```

Output: 
```
{
    "Response": {
        "RequestId": "602b2cf7-5499-446f-b7a7-cc62ae812fc6"
    }
}
```

