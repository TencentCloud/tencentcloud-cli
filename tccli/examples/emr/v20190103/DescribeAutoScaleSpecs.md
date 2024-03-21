**Example 1: 获取扩缩容规格成功示例**



Input: 

```
tccli emr DescribeAutoScaleSpecs --cli-unfold-argument  \
    --InstanceId emr-3ap64zl6
```

Output: 
```
{
    "Response": {
        "RequestId": "395ec6cd-1a51-41c1-a436-0ed4a5c8d74c",
        "SpecList": [
            {
                "CreateTime": "2019-12-26 17:17:06",
                "Id": 5,
                "PayMode": 0,
                "Priority": 1,
                "Resource": {
                    "Cpu": 2,
                    "DiskNum": 0,
                    "DiskSize": 100,
                    "DiskType": "CLOUD_PREMIUM",
                    "InstanceType": "S3.MEDIUM8",
                    "LocalDiskNum": 0,
                    "MemSize": 8192,
                    "MultiDisks": null,
                    "RootSize": 0,
                    "Spec": "CVM.S3",
                    "StorageType": 5,
                    "Tags": null
                }
            }
        ],
        "TotalCount": 1
    }
}
```

