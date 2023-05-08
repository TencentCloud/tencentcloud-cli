**Example 1: 获取数据表信息**



Input: 

```
tccli wedata DescribeTableInfoList --cli-unfold-argument  \
    --Catalog HIVE \
    --ConnectionType rpc \
    --Filters.0.Values 7 \
    --Filters.0.Name datasourceId \
    --Filters.1.Values hive \
    --Filters.1.Name type \
    --Filters.2.Values rost_test_hive384 \
    --Filters.2.Name databaseName
```

Output: 
```
{
    "Response": {
        "TableInfo": "xx",
        "RequestId": "xx"
    }
}
```

