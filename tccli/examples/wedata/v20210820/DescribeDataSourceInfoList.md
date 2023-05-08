**Example 1: 获取数据源信息**



Input: 

```
tccli wedata DescribeDataSourceInfoList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "DatasourceSet": [
            {
                "Name": "xx",
                "Region": "xx",
                "ClusterId": "xx",
                "DatabaseNames": [
                    "xx"
                ],
                "Instance": "xx",
                "Type": "xx",
                "ID": 1,
                "Description": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

