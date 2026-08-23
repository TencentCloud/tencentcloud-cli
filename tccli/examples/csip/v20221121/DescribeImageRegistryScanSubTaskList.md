**Example 1: 查询镜像仓库扫描子任务信息**



Input: 

```
tccli csip DescribeImageRegistryScanSubTaskList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --TaskId 2038
```

Output: 
```
{
    "Response": {
        "SubTaskList": [
            {
                "FailedReason": "",
                "ImageId": "sha256:6b56d305145037350b3aaa3a7cd7b818543875c8344436b0e2805778b859656e",
                "ImageName": "myimages_v7",
                "ImageRepoAddress": "172.**.*.**/csip-test/myimages_v7",
                "ImageTag": "1.0",
                "IsLatestImage": false,
                "OwnerAccountName": "***-管**",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "RegistryType": "harbor",
                "ScanStatus": "FINISHED",
                "Solution": "",
                "SubTaskId": 86411
            }
        ],
        "TotalCount": 4,
        "RequestId": "dbecc1fb-c925-4dec-b319-a20035390462"
    }
}
```

