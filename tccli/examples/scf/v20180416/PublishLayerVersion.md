**Example 1: 发布层版本**

发布层版本

Input: 

```
tccli scf PublishLayerVersion --cli-unfold-argument  \
    --LayerName abc \
    --CompatibleRuntimes abc \
    --Content.CosBucketName abc \
    --Content.CosObjectName abc \
    --Content.ZipFile abc \
    --Content.CosBucketRegion abc \
    --Content.DemoId abc \
    --Content.TempCosObjectName abc \
    --Content.GitUrl abc \
    --Content.GitUserName abc \
    --Content.GitPassword abc \
    --Content.GitPasswordSecret abc \
    --Content.GitBranch abc \
    --Content.GitDirectory abc \
    --Content.GitCommitId abc \
    --Content.GitUserNameSecret abc \
    --Content.ImageConfig.RegistryId abc \
    --Content.ImageConfig.ImageType abc \
    --Content.ImageConfig.ImageUri abc \
    --Content.ImageConfig.EntryPoint abc \
    --Content.ImageConfig.Command abc \
    --Content.ImageConfig.Args abc \
    --Content.ImageConfig.ContainerImageAccelerate True \
    --Description abc \
    --LicenseInfo abc
```

Output: 
```
{
    "Response": {
        "LayerVersion": 0,
        "RequestId": "abc"
    }
}
```

