**Example 1: 示例**



Input: 

```
tccli dsgc CreateDSPAMetaResources --cli-unfold-argument  \
    --DspaId dspa-ed415837 \
    --UpdateId 49f060ba-c12d-4643-98da-aa8bcc382091 \
    --UpdateStatus finished \
    --Items.0.BuildType xx \
    --Items.0.ResourceSyncTime xx \
    --Items.0.ResourceRegion xx \
    --Items.0.ResourceVip xx \
    --Items.0.MetaType xx \
    --Items.0.ResourceId xx \
    --Items.0.ResourceCreateTime xx \
    --Items.0.ResourceUniqueSubnetId xx \
    --Items.0.ResourceUniqueVpcId xx \
    --Items.0.ResourceName xx \
    --Items.0.AuthStatus xx \
    --Items.0.ResourceVPort 1 \
    --MetaType mariadb \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "6542ea46-5974-42b2-8876-f1ca946a92ce",
        "DspaId": "dspa-ed415837",
        "MetaType": "mariadb",
        "ResourceRegion": "ap-guangzhou",
        "UpdateId": "49f060ba-c12d-4643-98da-aa8bcc382091"
    }
}
```

