**Example 1: 展示镜像列表**

展示镜像列表

Input: 

```
tccli ecm DescribeImage --cli-unfold-argument  \
    --Offset 0\
    --Limit 10\
    --Filters.0.Name image-type\
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
                "ImageSize": 50
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
                "ImageSize": 50
            },
            {
                "ImageId": "img-31tjrtph",
                "ImageName": "CentOS 7.2 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 7.2 64位",
                "ImageDescription": "CentOS 7.2 64位",
                "Architecture": "x86_64",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 7.2 64位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            },
            {
                "ImageId": "img-6ns5om13",
                "ImageName": "CentOS 6.8 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 6.8 64位",
                "ImageDescription": "CentOS 6.8 64位",
                "Architecture": "x86_64",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 6.8 64位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            },
            {
                "ImageId": "img-6rrx0ymd",
                "ImageName": "Debian 9.0 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "Debian 9.0 64位",
                "ImageDescription": "Debian 9.0 64位",
                "Architecture": "x86_64",
                "OsType": "Debian",
                "Platform": "",
                "OsVersion": "Debian 9.0 64位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            },
            {
                "ImageId": "img-7uq6rrhr",
                "ImageName": "CentOS 6.5 32位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 6.5 32位",
                "ImageDescription": "CentOS 6.5 32位",
                "Architecture": "i386",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 6.5 32位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            },
            {
                "ImageId": "img-8toqc6s3",
                "ImageName": "CentOS 7.4 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 7.4 64位",
                "ImageDescription": "CentOS 7.4 64位",
                "Architecture": "x86_64",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 7.4 64位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            },
            {
                "ImageId": "img-9xwnxxn3",
                "ImageName": "Debian 7.8 32位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "Debian 7.8 32位",
                "ImageDescription": "Debian 7.8 32位",
                "Architecture": "i386",
                "OsType": "Debian",
                "Platform": "",
                "OsVersion": "Debian 7.8 32位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            },
            {
                "ImageId": "img-d5304izr",
                "ImageName": "SUSE Linux Enterprise Server 12 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "SUSE Linux Enterprise Server 12 64位",
                "ImageDescription": "SUSE Linux Enterprise Server 12 64位",
                "Architecture": "x86_64",
                "OsType": "SUSE",
                "Platform": "",
                "OsVersion": "SUSE Linux Enterprise Server 12 64位",
                "ImageCreateTime": "2019-07-22 20:48:15",
                "ImageSize": 50
            },
            {
                "ImageId": "img-dkwyg6sr",
                "ImageName": "CentOS 7.3 64位",
                "ImageState": "NORMAL",
                "ImageType": "PRIVATE_IMAGE",
                "ImageOwner": 251006057,
                "ImageOsName": "CentOS 7.3 64位",
                "ImageDescription": "CentOS 7.3 64位",
                "Architecture": "x86_64",
                "OsType": "CentOS",
                "Platform": "",
                "OsVersion": "CentOS 7.3 64位",
                "ImageCreateTime": "2019-07-22 20:48:14",
                "ImageSize": 50
            }
        ],
        "TotalCount": 20
    }
}
```

