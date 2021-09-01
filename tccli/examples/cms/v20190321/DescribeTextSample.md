**Example 1: 查询文本样本库**

查询白库

Input: 

```
tccli cms DescribeTextSample --cli-unfold-argument  \
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
        "TextSampleSet": [
            {
                "Label": 1,
                "EvilType": 20002,
                "Content": "太子党",
                "Code": 0,
                "Status": 1,
                "CreatedAt": "2019-05-28 17:40:01"
            },
            {
                "Label": 1,
                "EvilType": 20002,
                "Content": "赵家党",
                "Code": 0,
                "Status": 1,
                "CreatedAt": "2019-05-28 17:40:01"
            }
        ]
    },
    "retcode": 0,
    "retmsg": "success"
}
```

