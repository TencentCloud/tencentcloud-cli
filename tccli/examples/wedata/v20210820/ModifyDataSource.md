**Example 1: 样例**



Input: 

```
tccli wedata ModifyDataSource --cli-unfold-argument  \
    --ID 1 \
    --BizParams string \
    --Category DB \
    --DatabaseName string \
    --Description string \
    --Display string \
    --Name string \
    --Params string \
    --ClusterId string \
    --Status 1 \
    --Type CLICKHOUSE \
    --Collect string \
    --OwnerProjectId string \
    --OwnerProjectName string \
    --OwnerProjectIdent string \
    --COSBucket string \
    --COSRegion string
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": true
    }
}
```

