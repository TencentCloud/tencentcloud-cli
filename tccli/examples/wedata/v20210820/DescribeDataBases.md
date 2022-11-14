**Example 1: 查询数据来源列表**



Input: 

```
tccli wedata DescribeDataBases --cli-unfold-argument  \
    --ProjectId xx \
    --DatasourceId xx
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "InstanceId": "xx",
                "DatasourceId": "xx",
                "DatabaseId": "xx",
                "DatasourceName": "xx",
                "DatabaseName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

