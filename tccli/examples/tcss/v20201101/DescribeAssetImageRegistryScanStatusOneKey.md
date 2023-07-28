**Example 1: 镜像仓库查询一键镜像扫描状态**

镜像仓库查询一键镜像扫描状态

Input: 

```
tccli tcss DescribeAssetImageRegistryScanStatusOneKey --cli-unfold-argument  \
    --All True \
    --TaskID 1
```

Output: 
```
{
    "Response": {
        "ImageTotal": 1,
        "ImageScanCnt": 1,
        "ImageStatus": [
            {
                "ImageId": "abc",
                "RegistryType": "abc",
                "ImageRepoAddress": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "Namespace": "abc",
                "ImageName": "abc",
                "ImageTag": "abc",
                "ScanStatus": "abc",
                "CveProgress": 1,
                "RiskProgress": 1,
                "VirusProgress": 1
            }
        ],
        "SuccessCount": 1,
        "RiskCount": 1,
        "Schedule": 1,
        "Status": "abc",
        "ScanRemainTime": 1,
        "RequestId": "abc"
    }
}
```

**Example 2: 正常请求**

正常请求

Input: 

```
tccli tcss DescribeAssetImageRegistryScanStatusOneKey --cli-unfold-argument  \
    --TaskID 13
```

Output: 
```
{
    "Response": {
        "ImageScanCnt": 0,
        "ImageStatus": [],
        "ImageTotal": 1525,
        "RequestId": "a8298892-31c6-4a39-84e2-ce998b5822fd",
        "RiskCount": 0,
        "ScanRemainTime": 0,
        "Schedule": 0,
        "Status": "SCANNING",
        "SuccessCount": 0
    }
}
```

