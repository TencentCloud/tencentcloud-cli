**Example 1: 1**

1

Input: 

```
tccli wedata DescribeFieldBasicInfo --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc
```

Output: 
```
{
    "Response": {
        "ColumnBasicInfoList": [
            {
                "TableId": "abc",
                "DatasourceId": "abc",
                "DatasourceName": "abc",
                "DatabaseId": "abc",
                "DatabaseName": "abc",
                "TableName": "abc",
                "ColumnName": "abc",
                "DataType": "abc",
                "ColumnType": "abc",
                "ColumnDefault": "abc",
                "ColumnKey": "abc",
                "ColumnPosition": 0,
                "ColumnComment": "abc",
                "StoreType": "abc",
                "ProjectId": "abc",
                "ProjectName": "abc",
                "ProjectDisplayName": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

**Example 2: 错误1**

错误1

Input: 

```
tccli wedata DescribeFieldBasicInfo --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name 1 \
    --Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "76e7bf2b-c516-4a4c-97ba-f0b788097c1f"
    }
}
```

**Example 3: 错误2**

错误2

Input: 

```
tccli wedata DescribeFieldBasicInfo --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name 1 \
    --Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "235a9ac1-1037-4f8a-befe-9765a29480cd"
    }
}
```

