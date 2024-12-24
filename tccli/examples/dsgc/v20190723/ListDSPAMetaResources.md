**Example 1: 获取Dspa实例下数据源信息**

获取Dspa实例下的资源信息

Input: 

```
tccli dsgc ListDSPAMetaResources --cli-unfold-argument  \
    --DspaId dspa-6fb60936 \
    --Filters.0.Name ResourceId \
    --Filters.0.Values mariadb-9loqa8ed
```

Output: 
```
{
    "Response": {
        "DspaId": "dspa-a1b2dc78",
        "Resources": [
            {
                "ResourceId": "mariadb-3578e092",
                "ResourceName": "test123",
                "ResourceVip": "172.16.0.12",
                "ResourceVPort": 3306,
                "ResourceCreateTime": "2022-01-02 15:04:05",
                "ResourceUniqueVpcId": "vpc-73299612",
                "ResourceUniqueSubnetId": "subnet-awkdpmnn",
                "MetaType": "mariadb",
                "ResourceRegion": "ap-guangzhou",
                "ResourceSyncTime": "2022-01-02 15:04:05",
                "AuthStatus": "authorized",
                "BuildType": "cloud",
                "MasterInsId": "cdb-a1",
                "ResourceVpcId": 1,
                "ResourceSubnetId": 1,
                "Protocol": "mysql",
                "ResourceVersion": "10.2.3",
                "ResourceAuthType": "auto",
                "ResourceAuthAccount": "test123",
                "InstanceType": "mariadb",
                "InstanceValue": "mariadb-78693a6c",
                "GovernAuthStatus": 0,
                "AuthRange": "manual"
            }
        ],
        "TotalCount": 1,
        "RequestId": "715f6d81-d277-4f90-8089-f4d048a629d4"
    }
}
```

