**Example 1: 获取数据源信息**

获取数据源列表

Input: 

```
tccli wedata DescribeDataSourceInfoList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --ProjectId 1 \
    --Type MYSQL
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "DatasourceSet": [
            {
                "DatabaseNames": [
                    "default"
                ],
                "Description": "备注",
                "ID": 1,
                "Instance": "cdb-sd56gs51",
                "Name": "myst_test",
                "Region": "ap-beijing",
                "Type": "mysql",
                "ClusterId": "cdb-sf78f",
                "Version": "5.2.3",
                "ParamsString": "string"
            }
        ],
        "RequestId": "asdg15-asgg48as-sdg4861-516"
    }
}
```

