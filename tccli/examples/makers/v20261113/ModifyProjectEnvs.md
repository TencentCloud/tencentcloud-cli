**Example 1: 编辑项目环境变量**



Input: 

```
tccli makers ModifyProjectEnvs --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --EnvVars.0.Key CAPI_TEST \
    --EnvVars.0.Value 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3fd4d1f8-4c72-4679-89ed-2d3ce85a1b19"
    }
}
```

