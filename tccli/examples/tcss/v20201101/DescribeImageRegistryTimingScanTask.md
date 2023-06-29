**Example 1: 镜像仓库查看定时任务**

镜像仓库查看定时任务

Input: 

```
tccli tcss DescribeImageRegistryTimingScanTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f60f0ef9-a105-4535-8dfd-42ad8b3a9c73",
        "ScanTime": "03:00:00",
        "ScanPeriod": 1,
        "ScanType": [
            "risk",
            "virus"
        ],
        "All": false,
        "Images": [
            {
                "ImageDigest": "sha256:1319b1eaa0b7bcebae63af321fa67559b9517e8494060403d083bb3508fe52c8",
                "RegistryType": "ccr",
                "ImageRepoAddress": "ccr.ccs.tencentyun.com/yunding/luping:v1",
                "InstanceId": "",
                "InstanceName": "",
                "Namespace": "",
                "ImageName": "yunding/luping",
                "ImageTag": "v1",
                "Force": ""
            }
        ],
        "Id": [
            1
        ],
        "Enable": true,
        "Latest": true
    }
}
```

