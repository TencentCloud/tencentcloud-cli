**Example 1: 查询镜像扫描状态**

查询镜像扫描状态

Input: 

```
tccli tcss DescribeAssetImageScanStatus --cli-unfold-argument  \
    --TaskID dskaldjskld
```

Output: 
```
{
    "Response": {
        "ImageScanCnt": 0,
        "ImageTotal": 339,
        "LeftSeconds": 4666,
        "RequestId": "b9e9e86e-5b7e-476c-9be1-a8c6399afef3",
        "RiskCount": 0,
        "Schedule": 0,
        "Status": "SCANNING",
        "SuccessCount": 0
    }
}
```

