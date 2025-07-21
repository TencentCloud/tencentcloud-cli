**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli ctsdb DescribeDatabases --cli-unfold-argument  \
    --Database.ClusterID ctsdbi-xxxxxxx \
    --Database.Name 测试 \
    --Database.CoolDownInDays 0 \
    --Database.RetentionInDays 0 \
    --Database.Remark  \
    --Database.Status 0 \
    --Database.CreatedAt 2020-09-22T00:00:00+00:00 \
    --Database.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "ClusterID": "ctsdbi-xxxxxxx",
                "Name": "testData",
                "CoolDownInDays": 0,
                "RetentionInDays": 0,
                "Remark": "test",
                "Status": 0,
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "UpdatedAt": "2020-09-22T00:00:00+00:00"
            }
        ],
        "TotalCount": 0,
        "RequestId": "requestxxxxxxxxx"
    }
}
```

