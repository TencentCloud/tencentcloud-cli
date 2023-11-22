**Example 1: 查询表的所有列元数据**



Input: 

```
tccli wedata DescribeColumnsMeta --cli-unfold-argument  \
    --PageSize 0 \
    --IsPartitionQuery True \
    --OrderFieldSet.0.Direction xx \
    --OrderFieldSet.0.Name xx \
    --PageNumber 0 \
    --TableId xx \
    --FilterSet.0.Values xx \
    --FilterSet.0.Name xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ColumnMetaSet": [
            {
                "Description": "xx",
                "NameCn": "xx",
                "ColumnFamiliesFieldSet": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "IsPartition": true,
                "Position": 0,
                "NameEn": "xx",
                "Type": "xx",
                "Name": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

