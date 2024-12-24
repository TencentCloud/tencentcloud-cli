**Example 1: 示例**

添加用户云上资源列表示例

Input: 

```
tccli dsgc CreateDSPAMetaResources --cli-unfold-argument  \
    --DspaId dspa-ed415837 \
    --UpdateId 49f060ba-c12d-4643-98da-aa8bcc382091 \
    --UpdateStatus finished \
    --Items.0.ResourceVip 127.0.0.1 \
    --Items.0.ResourceId cdb-16cb45g7 \
    --Items.0.ResourceCreateTime 2022-12-03 10:42:19 \
    --Items.0.ResourceUniqueSubnetId subnet-xx \
    --Items.0.ResourceUniqueVpcId vpc-xx \
    --Items.0.ResourceName name \
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

