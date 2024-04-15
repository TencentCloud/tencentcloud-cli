**Example 1: 样例**



Input: 

```
tccli wedata DescribeDatasource --cli-unfold-argument  \
    --Id 1065 \
    --Env production
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatabaseName": "defalut",
            "Description": "dec",
            "ID": 1065,
            "Instance": "cdb-s778sf",
            "Name": "mysql1",
            "Region": "beijing",
            "Type": "mysql",
            "ClusterId": "cdb-sf78sf",
            "AppId": 1065994488,
            "BizParams": "string",
            "Category": "string",
            "Display": "mysql_test",
            "OwnerAccount": "12315",
            "Params": "string",
            "Status": 1,
            "OwnerAccountName": "name",
            "ClusterName": "cdb-sdhusf",
            "OwnerProjectId": "10356894654",
            "OwnerProjectName": "project1",
            "OwnerProjectIdent": "project1",
            "AuthorityProjectName": "project",
            "AuthorityUserName": "xiaoming",
            "Edit": true,
            "Author": true,
            "Deliver": true,
            "DataSourceStatus": "Unavailable",
            "CreateTime": 1712822907809,
            "ParamsString": "string",
            "BizParamsString": "string",
            "ModifiedTime": 1712822907809,
            "ShowType": "mysql",
            "ProductId": 1023,
            "DevelopmentId": 1,
            "DevelopmentParams": "string"
        },
        "RequestId": "asf156-asdg4861adg-5a81g"
    }
}
```

