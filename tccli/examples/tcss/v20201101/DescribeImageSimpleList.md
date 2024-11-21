**Example 1: 查询全部镜像列表**



Input: 

```
tccli tcss DescribeImageSimpleList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ImageCnt": 1,
        "ImageList": [
            {
                "Size": 1,
                "ImageName": "centos:7.6",
                "ContainerCnt": 0,
                "ImageType": "",
                "ImageID": "c826b9fa-68b5-4603-bf25-a5eb9b65c768"
            }
        ],
        "RequestId": "965c55c5-8ab1-4e32-8425-4c44acb5edec"
    }
}
```

