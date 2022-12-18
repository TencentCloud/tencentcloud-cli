**Example 1: 导出自定义镜像**

导出自定义镜像

Input: 

```
tccli cvm ExportImages --cli-unfold-argument  \
    --ImageIds img-72n9mi0y \
    --BucketName test-bucket-AppId
```

Output: 
```
{
    "Response": {
        "RequestId": "7995cb6f-0018-4286-a4d4-b6301b962d9e",
        "TaskId": 105591590,
        "CosPaths": [
            "/img-pq5pau1w_system_snap-fiux4bof.raw"
        ]
    }
}
```

