**Example 1: 展示镜像列表**

展示镜像列表

Input: 

```
tccli ecm DescribeImage --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name image-type \
    --Filters.0.Values PRIVATE_IMAGE
```

Output: 
```
{
    "Response": {
        "RequestId": "51e18e32-9bb8-4b1d-a7ac-92040fab2949",
        "ImageSet": [
            {
                "ImageId": "img-060ov1xz",
                "ImageName": "CentOS 6.9 32位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 6.9 32位",
                "ImageDescription": "CentOS 6.9 32位",
                "Architecture": "i386",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 6.9 32位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50,
                "ImageSource": "CREATE_IMAGE",
                "SrcImage": {
                    "ImageDescription": "CentOS 6.9 32位",
                    "InstanceId": "ein-gwht9ek2",
                    "Region": "ap-chongqing-ecm2",
                    "RegionID": 1084,
                    "ImageId": "img-cho4vg0s",
                    "ImageName": "test",
                    "RegionName": "重庆二区",
                    "InstanceName": "",
                    "ImageType": "PRIVATE_IMAGE",
                    "ImageOsName": "CentOS 6.9 32位"
                }
            },
            {
                "ImageId": "img-1tyt4apn",
                "ImageName": "CentOS 7.4 裸金属 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 7.4 裸金属 64位",
                "ImageDescription": "CentOS 7.4 裸金属 64位",
                "Architecture": "x86_64",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 7.4 裸金属 64位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50,
                "ImageSource": "EXTERNAL_IMPORT",
                "SrcImage": {
                    "ImageDescription": "",
                    "InstanceId": "",
                    "Region": "",
                    "RegionID": 0,
                    "ImageId": "",
                    "ImageName": "CentOS 7.4 64位",
                    "RegionName": "",
                    "InstanceName": "",
                    "ImageType": "",
                    "ImageOsName": "CentOS 7.4 64位"
                }
            }
        ],
        "TotalCount": 20
    }
}
```

