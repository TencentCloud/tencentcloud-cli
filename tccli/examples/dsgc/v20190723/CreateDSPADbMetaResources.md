**Example 1: 示例**

添加用户云上数据库类型资源

Input: 

```
tccli dsgc CreateDSPADbMetaResources --cli-unfold-argument  \
    --DspaId abc \
    --MetaType abc \
    --ResourceRegion abc \
    --UpdateStatus abc \
    --UpdateId abc \
    --Items.0.ResourceId abc \
    --Items.0.ResourceName abc \
    --Items.0.ResourceVip abc \
    --Items.0.ResourceVPort 1 \
    --Items.0.ResourceCreateTime abc \
    --Items.0.ResourceUniqueVpcId abc \
    --Items.0.ResourceUniqueSubnetId abc
```

Output: 
```
{
    "Response": {
        "UpdateId": "abc",
        "MetaType": "abc",
        "DspaId": "abc",
        "ResourceRegion": "abc",
        "RequestId": "abc"
    }
}
```

