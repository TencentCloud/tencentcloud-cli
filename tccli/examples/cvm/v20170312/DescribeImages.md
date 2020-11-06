**Example 1: Querying an image by its image ID**

This example shows you how to query the information on an image by the image ID.

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
                "ImageOsName": "centos6.6x86_32",
                "ImageType": "PUBLIC_IMAGE",
                "ImageCreateTime": "1970-01-01T00:00:00+00:00",
                "ImageStatus": "NORMAL",
                "ImageName": "CentOS 6.6 32-bit",
                "ImageDescription": "CentOS 6.6 32-bit",
                "Creator": "PUBLIC"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
```

**Example 2: Querying images by image type**

This example shows you how to query all private images under an account.

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
                "ImageOsName": "centos6.6x86_32",
                "ImageType": "PUBLIC_IMAGE",
                "ImageCreateTime": "1970-01-01T00:00:00+00:00",
                "ImageStatus": "NORMAL",
                "ImageName": "CentOS 6.6 32-bit",
                "ImageDescription": "CentOS 6.6 32-bit",
                "Creator": "PUBLIC"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
```

