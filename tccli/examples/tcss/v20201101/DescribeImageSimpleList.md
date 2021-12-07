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
                "ImageName": "xx",
                "ContainerCnt": 0,
                "ImageType": "xx",
                "ImageID": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

