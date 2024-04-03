**Example 1: 失败**

失败

Input: 

```
tccli wedata DescribeColumnsMeta --cli-unfold-argument  \
    --TableId 111 \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "DescribeColumnsMeta出错了，原因：元数据 MetaDataClient.describeColumnPageByTableName 接口出错了"
        },
        "RequestId": "9eba5f8a-8cf5-4ce1-a557-b5d8e624a9b9"
    }
}
```

**Example 2: 失败2**

失败2

Input: 

```
tccli wedata DescribeColumnsMeta --cli-unfold-argument  \
    --TableId 1 \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "DescribeColumnsMeta出错了，原因：元数据 MetaDataClient.describeColumnPageByTableName 接口出错了"
        },
        "RequestId": "964be7a0-7dde-4a2f-8a53-fa60524f87f8"
    }
}
```

**Example 3: 查询表的所有列元数据**



Input: 

```
tccli wedata DescribeColumnsMeta --cli-unfold-argument  \
    --TableId abc \
    --PageNumber 0 \
    --PageSize 0 \
    --FilterSet.0.Name abc \
    --FilterSet.0.Values abc \
    --OrderFieldSet.0.Name abc \
    --OrderFieldSet.0.Direction abc \
    --IsPartitionQuery True \
    --ComplianceId 0
```

Output: 
```
{
    "Response": {
        "ColumnMetaSet": [
            {
                "NameEn": "abc",
                "NameCn": "abc",
                "Type": "abc",
                "Description": "abc",
                "Position": 0,
                "IsPartition": true,
                "Name": "abc",
                "ColumnFamiliesFieldSet": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "DictionaryId": "abc",
                "DictionaryName": "abc",
                "LevelName": "abc",
                "LevelRank": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

