**Example 1: 查询镜像仓库定时扫描任务预览**



Input: 

```
tccli csip DescribeImageRegistryTimedScanTaskPreview --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --TaskId 1123 \
    --TargetType MANUAL_CONFIG
```

Output: 
```
{
    "Response": {
        "Images": [
            {
                "Id": 43428,
                "ImageId": "sha256*************0433f2e69028fdbdaae4bf922ead8af36db5d60fa1523b49f6cc",
                "ImageName": "myimages-v05",
                "ImageRepoAddress": "43.***.**.***:****/****-test/myimages-v05",
                "ImageTag": "v05",
                "IsLatestImage": true,
                "OwnerAccountName": "多**-管理*",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "RegistryType": "harbor"
            }
        ],
        "PreviewUpdatedAt": "2026-08-12T20:43:06+08:00",
        "TotalCount": 9,
        "RequestId": "aa0dade0-d8e0-4488-8a3e-ac00ee4e817d"
    }
}
```

