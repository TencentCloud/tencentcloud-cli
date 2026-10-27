**Example 1: DescribeImages**



Input: 

```
tccli cvd DescribeImages --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 20 \
    --Filters.0.Name InstanceType \
    --Filters.0.Values G6L.8XLARGE96
```

Output: 
```
{
    "Response": {
        "Images": [
            {
                "CoreType": "GPU_GC50",
                "CreateTime": "2026-07-03 16:15:01",
                "CvmImageId": "img-***g3fob",
                "DataDiskSize": 0,
                "Description": "",
                "ImageID": "img-***g3fob",
                "ImageName": "********Windows Server 2019 数据中心版 64位中文版",
                "ImageSize": 50,
                "ImageState": "NORMAL",
                "ImageType": "PUBLIC_IMAGE",
                "IsWhole": false,
                "OsName": "Windows Server 2019-64位",
                "Region": "ap-shanghai"
            }
        ],
        "Total": 1,
        "RequestId": "308a0c9b-7b46-4bbf-8945-2eddee56b237"
    }
}
```

