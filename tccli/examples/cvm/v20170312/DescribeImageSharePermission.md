**Example 1: 查看指定镜像的分享信息**

查看镜像img-6pb6lrmy的分享信息。

Input: 

```
tccli cvm DescribeImageSharePermission --cli-unfold-argument  \
    --ImageId img-6pb6lrmy
```

Output: 
```
{
    "Response": {
        "SharePermissionSet": [
            {
                "CreatedTime": "2018-06-10T11:02:50Z",
                "AccountId": "101104350000"
            },
            {
                "CreatedTime": "2018-06-13T15:03:25Z",
                "AccountId": "101104350001"
            }
        ],
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

