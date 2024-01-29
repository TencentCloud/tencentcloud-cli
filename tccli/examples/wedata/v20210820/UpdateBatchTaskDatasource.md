**Example 1: 失败**

失败

Input: 

```
tccli wedata UpdateBatchTaskDatasource --cli-unfold-argument  \
    --TaskIds 20230608210301228 \
    --DatasourceId 123 \
    --DatasourceType oracle \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "4bde7b6e-a7f3-49d4-a7fc-46c1056f2d17"
    }
}
```

**Example 2: 成功**

成功

Input: 

```
tccli wedata UpdateBatchTaskDatasource --cli-unfold-argument  \
    --TaskIds abc \
    --DatasourceId abc \
    --DatasourceType abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 3: 成功2**

成功2

Input: 

```
tccli wedata UpdateBatchTaskDatasource --cli-unfold-argument  \
    --TaskIds 1470547050521227264 \
    --DatasourceId 8452 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 4: 成功示例**



Input: 

```
tccli wedata UpdateBatchTaskDatasource --cli-unfold-argument  \
    --TaskIds abc \
    --DatasourceId abc \
    --DatasourceType abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

