**Example 1: 获取云托管代码上传url**

通过环境id,获得云托管代码上传url, 用来上传代码

Input: 

```
tccli tcb DescribeCloudBaseBuildService --cli-unfold-argument  \
    --EnvId cdnheader-v2a \
    --ServiceName nginx-test
```

Output: 
```
{
    "Response": {
        "DownloadHeaders": [
            {
                "Value": "xx",
                "Key": "xx"
            }
        ],
        "UploadHeaders": [
            {
                "Value": "xx",
                "Key": "xx"
            }
        ],
        "UploadUrl": "xx",
        "DownloadUrl": "xx",
        "RequestId": "xx",
        "OutDate": true,
        "PackageVersion": "xx",
        "PackageName": "xx"
    }
}
```

