**Example 1: 发布层版本**



Input: 

```
tccli scf PublishLayerVersion --cli-unfold-argument  \
    --Description xx \
    --LicenseInfo xx \
    --Content.GitUserName xx \
    --Content.TempCosObjectName xx \
    --Content.DemoId xx \
    --Content.ZipFile xx \
    --Content.GitUrl xx \
    --Content.GitUserNameSecret xx \
    --Content.GitCommitId xx \
    --Content.CosObjectName xx \
    --Content.GitBranch xx \
    --Content.GitPassword xx \
    --Content.CosBucketRegion xx \
    --Content.CosBucketName xx \
    --Content.GitDirectory xx \
    --Content.GitPasswordSecret xx \
    --CompatibleRuntimes xx \
    --LayerName xx
```

Output: 
```
{
    "Response": {
        "LayerVersion": 1,
        "RequestId": "xx"
    }
}
```

