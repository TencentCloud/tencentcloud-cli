**Example 1: 获取数据源信息**

获取数据源列表

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
                "DatabaseNames": [
                    "abc"
                ],
                "Description": "abc",
                "ID": 1,
                "Instance": "abc",
                "Name": "abc",
                "Region": "abc",
                "Type": "abc",
                "ClusterId": "abc",
                "Version": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

