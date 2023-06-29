**Example 1: 查询容器组件列表**



Input: 

```
tccli tcss DescribeAssetComponentList --cli-unfold-argument  \
    --ContainerID dnhaidhkahdjas
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Name": "zlib",
                "Version": "1.2.11-r0;apk;;"
            },
            {
                "Name": "apk-tools",
                "Version": "2.7.6-r0;apk;;"
            }
        ],
        "RequestId": "8341b3a1-8bb3-43ad-a56e-30e265be1a97",
        "TotalCount": 14
    }
}
```

