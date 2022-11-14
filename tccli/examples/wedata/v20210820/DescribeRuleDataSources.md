**Example 1: 查询质量规则数据源**



Input: 

```
tccli wedata DescribeRuleDataSources --cli-unfold-argument  \
    --ProjectId xx \
    --DatasourceId xx
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DatabaseId": "xx",
                "DatasourceName": "xx",
                "InstanceId": "xx",
                "DatasourceType": 1,
                "DatasourceId": "xx",
                "DatabaseName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

