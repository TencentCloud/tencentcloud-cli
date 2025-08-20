**Example 1: 创建投递规则**

用于创建cos投递任务规则

Input: 

```
tccli cls CreateShipper --cli-unfold-argument  \
    --TopicId fadcc986-xxxx-xxxx-b766-9ce9c193da32 \
    --Bucket examplebucket-1250000000 \
    --Prefix bow-test-1250000000 \
    --ShipperName bow-投递任务 \
    --Interval 300 \
    --MaxSize 5 \
    --FilenameMode 1 \
    --FilterRules.0.Key http \
    --FilterRules.0.Regex ^(\d+\.\d+)\..* \
    --FilterRules.0.Value 172.16 \
    --Partition /%Y/%m/%d/%H/ \
    --Compress.Format none \
    --RoleArn  \
    --ExternalId  \
    --Content.Format json \
    --Content.Json.EnableTag True \
    --Content.Json.MetaFields __SOURCE__ __FILENAME__ __HOSTNAME__ __TIMESTAMP__ \
    --Content.Json.JsonType 1 \
    --StartTime 1735544418 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3d8b7942-xxxx-xxxx-8c14-7c665344223c",
        "ShipperId": "a851ee81-xxxx-xxxx-852d-55fa5ac58269"
    }
}
```

