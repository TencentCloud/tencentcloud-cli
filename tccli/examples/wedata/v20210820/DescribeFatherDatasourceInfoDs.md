**Example 1: 成功**

成功

Input: 

```
tccli wedata DescribeFatherDatasourceInfoDs --cli-unfold-argument  \
    --ProjectId abc \
    --PageNum 1 \
    --PageSize 1 \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 1,
            "Items": [
                {
                    "TaskName": "abc",
                    "TaskId": "abc",
                    "DatasourceName": "abc",
                    "DatasourceId": "abc",
                    "DatasourceType": "abc"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "abc"
    }
}
```

