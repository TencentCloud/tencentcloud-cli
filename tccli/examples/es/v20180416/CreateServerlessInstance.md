**Example 1: 创建serverless实例**

创建serverless实例

Input: 

```
tccli es CreateServerlessInstance --cli-unfold-argument  \
    --Zone ap-nanjing-1 \
    --VpcId vpc-dafafefe \
    --SubnetId subnet-faefeffe \
    --IndexName index_search \
    --IndexMetaJson {"mappings":{"properties":{}},"options":{"expire.max_age":"3d","timestamp_field":"@timestamp"},"settings":{}} \
    --SpaceId space-dadaefef \
    --Username user \
    --Password affwaiUINbc
```

Output: 
```
{
    "Response": {
        "InstanceId": "index-faefaf",
        "DealName": "20250320244403348150491",
        "RequestId": "6b044118-0566-11f0-b68a-5254001dee24 "
    }
}
```

