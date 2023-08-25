**Example 1: 示例**

获取Dspa实例下的指定cdb资源信息

Input: 

```
tccli dsgc ListDSPAMetaResources --cli-unfold-argument  \
    --DspaId dspa-6fb60936 \
    --Filters.0.Name ResourceId \
    --Filters.0.Values cdb-9loqa8ed
```

Output: 
```
{
    "Response": {
        "RequestId": "0b727eb5-5759-40c2-adeb-bb238e0259db",
        "TotalCount": 1,
        "DspaId": "dspa-6fb60936",
        "Resources": [
            {
                "BuildType": "cloud",
                "MetaType": "cdb",
                "ResourceId": "cdb-9loqa8ed",
                "ResourceName": "永久勿删-分类分级自动化测试使用",
                "ResourceRegion": "ap-guangzhou",
                "ResourceVip": "172.16.0.24",
                "ResourceVPort": 3306,
                "ResourceSyncTime": "2022-06-27 10:22:51",
                "ResourceCreateTime": "2022-06-08 10:48:20",
                "AuthStatus": "authorized",
                "ResourceUniqueVpcId": "vpc-7vv1q6x9",
                "ResourceUniqueSubnetId": "subnet-n488vg8m",
                "ResourceSubnetId": 0,
                "ResourceVpcId": 0,
                "MasterInsId": "cdb-9loqa8ed",
                "Protocol": "mysql"
            }
        ]
    }
}
```

