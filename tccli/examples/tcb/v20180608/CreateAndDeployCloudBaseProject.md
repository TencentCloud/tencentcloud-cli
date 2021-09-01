**Example 1: 创建云开发项目**



Input: 

```
tccli tcb CreateAndDeployCloudBaseProject --cli-unfold-argument  \
    --EnvId xx \
    --Name xx \
    --Parameters.0.Value xx \
    --Parameters.0.Key xx \
    --Tags xx \
    --RcJson xx \
    --FreeQuota xx \
    --NetworkConfig xx \
    --Source.CodingPackageVersion xx \
    --Source.WorkDir xx \
    --Source.Name xx \
    --Source.Url xx \
    --Source.RawCode xx \
    --Source.Type xx \
    --Source.CodingPackageName xx \
    --AddonConfig xx \
    --EnvAlias xx \
    --Type xx
```

Output: 
```
{
    "Response": {
        "EnvId": "xx",
        "RequestId": "xx"
    }
}
```

