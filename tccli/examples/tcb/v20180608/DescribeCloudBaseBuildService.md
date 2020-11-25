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
        "RequestId": "xx",
        "UploadHeaders": [
            {
                "Value": "xx",
                "Key": "xx"
            }
        ],
        "PackageVersion": "xx",
        "PackageName": "xx",
        "UploadUrl": "xx"
    }
}
```

