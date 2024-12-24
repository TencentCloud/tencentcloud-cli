**Example 1: 示例**

添加用户云上数据库类型资源

Input: 

```
tccli dsgc CreateDSPADbMetaResources --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --MetaType cdb \
    --ResourceRegion ap-guangzhou \
    --UpdateStatus continue \
    --Items.0.ResourceId cdb-a1c3e78 \
    --Items.0.ResourceName test123 \
    --Items.0.ResourceVip 172.16.0.17 \
    --Items.0.ResourceVPort 3306 \
    --Items.0.ResourceCreateTime 2020-05-07 22:00:00 \
    --Items.0.ResourceUniqueVpcId vpc-sl18927c \
    --Items.0.ResourceUniqueSubnetId subnet-awkpmc3
```

Output: 
```
{
    "Response": {
        "MetaType": "cbd-a1c3d78",
        "DspaId": "dspa-a2e3d278",
        "RequestId": "18dafbf7-83d5-4159-aeaf-4a02f1975176"
    }
}
```

