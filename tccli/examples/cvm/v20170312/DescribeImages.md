**Example 1: 按镜像ID查询镜像**

已经知道镜像ID，查询镜像相关信息。

Input: 

```
tccli cvm DescribeImages --cli-unfold-argument  \
    --Filters.0.Name image-id \
    --Filters.0.Values img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-pmqg1cw7",
                "ImageType": "PUBLIC_IMAGE",
                "ImageName": "CentOS 6.6 32位",
                "ImageDescription": "CentOS 6.6 32位"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
```

**Example 2: 按镜像类型查询镜像**

查询账户下所有私有镜像。

Input: 

```
tccli cvm DescribeImages --cli-unfold-argument  \
    --Filters.0.Name image-type \
    --Filters.0.Values PRIVATE_IMAGE
```

Output: 
```
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-pmqg1cw7",
                "ImageType": "PUBLIC_IMAGE",
                "ImageName": "CentOS 6.6 32位",
                "ImageDescription": "CentOS 6.6 32位"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
```

