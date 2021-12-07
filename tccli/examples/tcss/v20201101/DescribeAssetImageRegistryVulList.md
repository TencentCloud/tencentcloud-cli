**Example 1: 镜像仓库查询镜像漏洞列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryVulList --cli-unfold-argument  \
    --ImageInfo.Force xx \
    --ImageInfo.ImageTag xx \
    --ImageInfo.InstanceId xx \
    --ImageInfo.RegistryType xx \
    --ImageInfo.Namespace xx \
    --ImageInfo.ImageRepoAddress xx \
    --ImageInfo.ImageName xx \
    --ImageInfo.ImageDigest xx \
    --ImageInfo.InstanceName xx \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4ffca7b7-3d73-4317-8a76-a2b00e90f3b2",
        "List": null,
        "TotalCount": 0
    }
}
```

