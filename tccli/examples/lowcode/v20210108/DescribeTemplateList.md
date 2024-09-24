**Example 1: yunapi-test**



Input: 

```
tccli lowcode DescribeTemplateList --cli-unfold-argument  \
    --PageIndex 1 \
    --Code 字符串 \
    --PageSize 1 \
    --AppCode 字符串 \
    --SourceList 1 \
    --EnvId 字符串 \
    --StateTag 字符串 \
    --AuthTag 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 0,
            "Rows": []
        },
        "RequestId": "db8e6d51-635d-48d9-ab0e-ddde79f6f18c"
    }
}
```

**Example 2: 查询外部数据源模板列表**



Input: 

```
tccli lowcode DescribeTemplateList --cli-unfold-argument  \
    --PageIndex 1 \
    --PageSize 1 \
    --Code abc \
    --EnvId abc \
    --StateTag abc \
    --AppCode abc \
    --SourceList 0 \
    --AuthTag 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Rows": [
                {
                    "Code": "abc",
                    "Name": "abc",
                    "Icon": "abc",
                    "Methods": "abc",
                    "Source": 0,
                    "CreateAt": "abc",
                    "UpdateAt": "abc",
                    "Description": "abc",
                    "AuthUrl": "abc"
                }
            ],
            "Count": 1
        },
        "RequestId": "abc"
    }
}
```

