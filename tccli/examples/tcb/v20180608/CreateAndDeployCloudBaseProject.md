**Example 1: 创建云开发项目**



Input: 

```
tccli tcb CreateAndDeployCloudBaseProject --cli-unfold-argument  \
    --EnvId env-absdsasda \
    --Name name \
    --Parameters.0.Value value \
    --Parameters.0.Key key \
    --Tags tag1 \
    --RcJson {"key":"value"} \
    --FreeQuota quota \
    --NetworkConfig {"key":"value"} \
    --RepoUrl http://repourl \
    --Source.CodingPackageVersion version \
    --Source.WorkDir dir \
    --Source.Name name \
    --Source.Url http://url \
    --Source.ProjectId 0 \
    --Source.RawCode rawCode \
    --Source.Branch branch \
    --Source.ProjectName projectName \
    --Source.Type type \
    --Source.CodingPackageName packageName \
    --AddonConfig {"key":"value"} \
    --AutoDeployOnCodeChange True \
    --EnvAlias env \
    --Type pre
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

