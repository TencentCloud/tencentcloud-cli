**Example 1: 示例**



Input: 

```
tccli dsgc CreateDSPASelfBuildMetaResource --cli-unfold-argument  \
    --DspaId dspa-6fb60936 \
    --MetaType postgre_like_proto \
    --Password casb2020 \
    --ResourceAccessType cvm \
    --ResourceId ins-xd48jxyk \
    --ResourceName 元数据管理自动化使用勿删-永久勿删 \
    --ResourceRegion ap-guangzhou \
    --ResourceUniqueSubnetId subnet-n488vg8m \
    --ResourceUniqueVpcId vpc-7vv1q6x9 \
    --ResourceVPort 5432 \
    --ResourceVip 172.16.0.45 \
    --UserName root
```

Output: 
```
{
    "Response": {
        "RequestId": "61e47c12-c480-424d-967d-353684c66c8a",
        "ConnectivityStatus": "success",
        "ConnectivityDescription": "success"
    }
}
```

