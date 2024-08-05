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
        "DspaId": "abc",
        "Resources": [
            {
                "ResourceId": "abc",
                "ResourceName": "abc",
                "ResourceVip": "abc",
                "ResourceVPort": 1,
                "ResourceCreateTime": "abc",
                "ResourceUniqueVpcId": "abc",
                "ResourceUniqueSubnetId": "abc",
                "MetaType": "abc",
                "ResourceRegion": "abc",
                "ResourceSyncTime": "abc",
                "AuthStatus": "abc",
                "BuildType": "abc",
                "MasterInsId": "abc",
                "ResourceVpcId": 1,
                "ResourceSubnetId": 1,
                "Protocol": "abc",
                "ResourceVersion": "abc",
                "ResourceAuthType": "abc",
                "ResourceAuthAccount": "abc",
                "InstanceType": "abc",
                "InstanceValue": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

