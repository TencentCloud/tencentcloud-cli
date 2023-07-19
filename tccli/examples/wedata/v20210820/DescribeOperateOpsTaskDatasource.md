**Example 1: 获取数据源列表**

任务运维-获取数据源列表

Input: 

```
tccli wedata DescribeOperateOpsTaskDatasource --cli-unfold-argument  \
    --ProjectId abc \
    --ServiceKind abc \
    --ServiceType abc \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DatabaseName": "abc",
                "Description": "abc",
                "ID": 1,
                "Instance": "abc",
                "Name": "abc",
                "Region": "abc",
                "Type": "abc",
                "ClusterId": "abc",
                "AppId": 1,
                "Category": "abc",
                "Display": "abc",
                "OwnerAccount": "abc",
                "Status": 1,
                "OwnerAccountName": "abc",
                "ClusterName": "abc",
                "OwnerProjectId": "abc",
                "OwnerProjectName": "abc",
                "OwnerProjectIdent": "abc",
                "Edit": true,
                "Author": true,
                "Deliver": true,
                "DataSourceStatus": "abc",
                "AuthorityProjectName": "abc",
                "AuthorityUserName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

