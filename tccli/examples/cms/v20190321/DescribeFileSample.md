**Example 1: 查询图片样本库**

查询黑图片样本库前20条内容，并按CreatedAt倒序排序

Input: 

```
tccli cms DescribeFileSample --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --OrderField CreatedAt \
    --OrderDirection desc \
    --Filters.0.Name Label \
    --Filters.0.Value 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c1935701-668a-4e0f-9f25-7e88a5f3f7af",
        "TotalCount": 10,
        "FileSampleSet": [
            {
                "Label": 1,
                "EvilType": 20002,
                "FileName": "1.png",
                "FileType": "image",
                "FileMd5": "",
                "Code": 0,
                "Status": 1,
                "CreatedAt": "2019-05-28 17:40:01"
            },
            {
                "Label": 1,
                "EvilType": 20002,
                "FileName": "2.png",
                "FileType": "image",
                "FileMd5": "",
                "Code": 0,
                "Status": 1,
                "CreatedAt": "2019-05-28 17:40:01"
            }
        ]
    }
}
```

