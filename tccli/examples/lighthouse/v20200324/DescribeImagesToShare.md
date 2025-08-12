**Example 1: 查询CVM的自定义镜像列表共享到轻量应用服务器**



Input: 

```
tccli lighthouse DescribeImagesToShare --cli-unfold-argument  \
    --ImageIds img-cs2rrmp0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ImageSet": [
            {
                "ImageId": "img-cs2rrmp0",
                "ImageName": "ubuntu",
                "ImageDescription": "ubuntu",
                "ImageSize": 50,
                "ImageSource": "CREATE_IMAGE",
                "ImageClass": "SystemImage",
                "ImageState": "NORMAL",
                "IsSupportCloudinit": true,
                "Architecture": "x86_64",
                "OsName": "Ubuntu Server 20.04 LTS 64bit",
                "Platform": "Ubuntu",
                "CreatedTime": "2021-07-23T08:49:36Z",
                "IsShareable": true,
                "UnshareableReason": ""
            }
        ],
        "RequestId": "c5aafa9d-20e4-400e-852c-b800f607dd91"
    }
}
```

