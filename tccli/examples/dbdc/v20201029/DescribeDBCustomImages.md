**Example 1: 查询 DB Custom 镜像列表**



Input: 

```
tccli dbdc DescribeDBCustomImages --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "ImageSet": [
            {
                "Architecture": "x86_64",
                "ImageId": "img-1tmhysjj",
                "ImageType": "PUBLIC_IMAGE",
                "OsName": "TencentOS Server 3.2 with Driver"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e25c30f8-c61e-4895-a8a9-1181389d2b74"
    }
}
```

