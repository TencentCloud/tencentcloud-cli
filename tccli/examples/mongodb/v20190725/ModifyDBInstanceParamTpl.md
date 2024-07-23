**Example 1: 修改参数**



Input: 

```
tccli mongodb ModifyDBInstanceParamTpl --cli-unfold-argument  \
    --Params.0.Key operation.profiling.slowOpThresholdMs \
    --Params.0.Value 1001 \
    --TplId tpl-2284g3nmw
```

Output: 
```
{
    "Response": {
        "RequestId": "55c81522-95ae-4dc1-a8a4-15b3efd06f36"
    }
}
```

