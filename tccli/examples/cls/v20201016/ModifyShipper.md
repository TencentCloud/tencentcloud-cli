**Example 1: 修改投递COS任务**

修改投递COS任务

Input: 

```
tccli cls ModifyShipper --cli-unfold-argument  \
    --ShipperId 2ac8a8aa-xxxx-xxxx-84cd-8cd2beeeae17 \
    --Bucket bucket-test-12541111 \
    --Prefix bow-test-12541111 \
    --ShipperName bow-test-shipper-12541111 \
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
    --Content.Json.MetaFields __SOURCE__ __FILENAME__ __TIMESTAMP__ __HOSTNAME__ \
    --Content.Json.JsonType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-xxxx-xxxx-bb20-270359fb54a7"
    }
}
```

**Example 2: 修改投递任务**

改为跨账号投递

Input: 

```
tccli cls ModifyShipper --cli-unfold-argument  \
    --ShipperId 3f9562a7-xxxx-xxxx-b32a-d51a927226a7 \
    --Bucket examplebucket-1250000000 \
    --Prefix bowtest-1250000000 \
    --ShipperName bow-test-1250000000 \
    --Interval 300 \
    --MaxSize 10 \
    --FilenameMode 1 \
    --FilterRules.0.Key http \
    --FilterRules.0.Regex ^(\d+\.\d+)\..* \
    --FilterRules.0.Value 172.16 \
    --Partition /%Y/%m/%d/%H/ \
    --Compress.Format gzip \
    --RoleArn qcs::cam::uin/123123123:roleName/uinA_writeCLS_to_COS \
    --ExternalId 123123123123123 \
    --Content.Format json \
    --Content.Json.EnableTag True \
    --Content.Json.MetaFields __SOURCE__ __FILENAME__ __TIMESTAMP__ __HOSTNAME__ \
    --Content.Json.JsonType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "25d826d2-xxxx-xxxx-a4b6-f5490e86ae81"
    }
}
```

