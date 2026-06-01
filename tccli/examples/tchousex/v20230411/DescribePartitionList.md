**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribePartitionList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --DbName test \
    --TableName t4 \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "DbName": "test",
                "Name": "imp_date=20240131",
                "TableName": "t4"
            },
            {
                "DbName": "test",
                "Name": "imp_date=20240201",
                "TableName": "t4"
            },
            {
                "DbName": "test",
                "Name": "imp_date=20240202",
                "TableName": "t4"
            }
        ],
        "RequestId": "36d3aa39-da1f-4793-b47c-f5480f7b4978",
        "TotalCount": 3
    }
}
```

