**Example 1: 创建云开发项目**



Input: 

```
tccli tcb CreateAndDeployCloudBaseProject --cli-unfold-argument  \
    --EnvId xx \
    --Name xx \
    --Parameters.0.Value xx \
    --Parameters.0.Key xx \
    --Tags None \
    --RcJson xx \
    --FreeQuota xx \
    --NetworkConfig xx \
    --RepoUrl xx \
    --Source.CodingPackageVersion xx \
    --Source.WorkDir xx \
    --Source.Name xx \
    --Source.Url xx \
    --Source.ProjectId 0 \
    --Source.RawCode xx \
    --Source.Branch xx \
    --Source.ProjectName xx \
    --Source.Type xx \
    --Source.CodingPackageName xx \
    --AddonConfig xx \
    --AutoDeployOnCodeChange True \
    --EnvAlias xx \
    --Type xx
```

Output: 
```
{
    "Response": {
        "EnvId": "lowcode-7ggmm27y1d0633a9",
        "RequestId": "00b9517e-7ba6-4b41-b0c3-4d50c64cef62"
    }
}
```

