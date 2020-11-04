**Example 1: 查询自定义词库接口示例**



Input: 

```
tccli nlp DescribeDict --cli-unfold-argument  \
    --DictId udf-066edc3449
```

Output: 
```
{
    "Response": {
        "Dicts": [
            {
                "Description": "王者荣耀4月份新增英雄人名",
                "CreateTime": "2020-05-12 08:10:15",
                "UpdateTime": "2020-05-12 08:10:52",
                "Id": "udf-066edc3449",
                "Name": "王者荣耀人名2"
            }
        ],
        "RequestId": "986c5ae4-d6e1-4e33-a7a3-baba21ad8aba"
    }
}
```

