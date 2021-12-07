**Example 1: 镜像仓库查询镜像高危行为列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryRiskInfoList --cli-unfold-argument  \
    --ImageInfo.Force xx \
    --ImageInfo.ImageTag xx \
    --ImageInfo.InstanceId xx \
    --ImageInfo.RegistryType xx \
    --ImageInfo.Namespace xx \
    --ImageInfo.ImageRepoAddress xx \
    --ImageInfo.ImageName xx \
    --ImageInfo.ImageDigest xx \
    --ImageInfo.InstanceName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "c283b995-d932-436d-8deb-11d2b7eb216c",
        "List": null,
        "TotalCount": 0
    }
}
```

