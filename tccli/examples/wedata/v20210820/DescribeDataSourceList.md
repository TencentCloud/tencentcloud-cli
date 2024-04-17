**Example 1: 样例**

查询数据源

Input: 

```
tccli wedata DescribeDataSourceList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "Rows": [
                {
                    "AppId": 1986419,
                    "Author": false,
                    "AuthorityProjectName": null,
                    "AuthorityUserName": null,
                    "BizParams": null,
                    "BizParamsString": "",
                    "Category": "DB",
                    "ClusterId": "d6sdfg-b0d1-4b2c-b0bb-3f19654f9ff0b0",
                    "ClusterName": null,
                    "CreateTime": 1712823453266555,
                    "DataSourceStatus": "Available",
                    "DatabaseName": "emall",
                    "Deliver": false,
                    "Description": "",
                    "DevelopmentId": null,
                    "DevelopmentParams": null,
                    "Display": "emall",
                    "Edit": false,
                    "ID": 563511,
                    "Instance": null,
                    "ModifiedTime": 1712264523812655,
                    "Name": "emall",
                    "OwnerAccount": "100034623548673",
                    "OwnerAccountName": "allenbguasdo",
                    "OwnerProjectId": "153160969233490365952",
                    "OwnerProjectIdent": "project1",
                    "OwnerProjectName": "[project1]",
                    "Params": null,
                    "ParamsString": "{\"vport\":\"63348\",\"connectType\":\"public\",\"ip\":\"156.16.156.156\",\"publicPort\":\"6658\",\"publicIp\":\"189.15.15\",\"type\":\"MYSQL\",\"authorityType\":\"true\",\"deployType\":\"CONNSTR_PUBLICDB\",\"url\":\"jdbc:mysql://156.15.161.65:63258/emall\",\"vurl\":\"jdbc:mysql://68.23.265.86:63618/emall\",\"password\":\"********\",\"vpcTenantId\":\"131506509\",\"port\":\"65113\",\"passwordEncrypt\":\"40de7fbe6ad34c9d581af31416ef2a6c\",\"publicUrl\":\"jdbc:mysql://32.13.26.23:66413/emall\",\"vip\":\"156.168.95.62\",\"db\":\"emall\",\"username\":\"sdggds\"}",
                    "ProductId": "59111",
                    "Region": "ap-beijing",
                    "ShowType": "MySQL",
                    "Status": 2,
                    "Type": "MYSQL"
                }
            ],
            "TotalCount": 1,
            "TotalPageNumber": null
        },
        "RequestId": "44266d40-5822-48b3-bf0f-74f5b06d98eb"
    }
}
```

