**Example 1: 查看自定义镜像列表**



Input: 

```
tccli bm DescribeCustomImages --cli-unfold-argument  \
    --Limit 3 \
    --Offset 0 \
    --SearchKey img \
    --OrderField CreateTime \
    --Order 0 \
    --ImageStatus 3
```

Output: 
```
{
    "Response": {
        "RequestId": "52e092d0-fd15-4867-a937-1978c139f26b",
        "TotalCount": 13,
        "CustomImageSet": [
            {
                "ImageId": "img-2cmi7d5z",
                "ImageName": "no-ping1233",
                "ImageStatus": 3,
                "OsClass": "Ubuntu",
                "OsVersion": "14",
                "OsBit": 64,
                "ImageSize": 485,
                "CreateTime": "2018-07-23 10:50:31",
                "DeviceClassCode": "PS100v1",
                "OsTypeId": 69,
                "ImageDescription": "机器",
                "PartitionInfoSet": [
                    {
                        "Name": "/dev/sda1",
                        "Size": 2048
                    },
                    {
                        "Name": "/dev/sda2",
                        "Size": 2048
                    },
                    {
                        "Name": "/dev/sda3",
                        "Size": 10240
                    },
                    {
                        "Name": "/dev/sda4",
                        "Size": 3126910
                    }
                ]
            },
            {
                "ImageId": "img-m57nhkdn",
                "ImageName": "centos6",
                "ImageStatus": 3,
                "OsClass": "Centos",
                "OsVersion": "6.8",
                "OsBit": 64,
                "ImageSize": 394,
                "CreateTime": "2018-07-27 14:55:39",
                "DeviceClassCode": "PS001v1",
                "OsTypeId": 77,
                "ImageDescription": "",
                "PartitionInfoSet": [
                    {
                        "Name": "/dev/sda1",
                        "Size": 2048
                    },
                    {
                        "Name": "/dev/sda2",
                        "Size": 22528
                    },
                    {
                        "Name": "/dev/sda3",
                        "Size": 2048
                    },
                    {
                        "Name": "/dev/sda4",
                        "Size": 830078
                    }
                ]
            },
            {
                "ImageId": "img-5tws80gz",
                "ImageName": "ssh-port",
                "ImageStatus": 3,
                "OsClass": "Centos",
                "OsVersion": "6.8",
                "OsBit": 64,
                "ImageSize": 394,
                "CreateTime": "2018-07-27 16:02:56",
                "DeviceClassCode": "PS001v1",
                "OsTypeId": 77,
                "ImageDescription": "",
                "PartitionInfoSet": [
                    {
                        "Name": "/dev/sda1",
                        "Size": 2048
                    },
                    {
                        "Name": "/dev/sda2",
                        "Size": 22528
                    },
                    {
                        "Name": "/dev/sda3",
                        "Size": 2048
                    },
                    {
                        "Name": "/dev/sda4",
                        "Size": 830078
                    }
                ]
            }
        ]
    }
}
```

