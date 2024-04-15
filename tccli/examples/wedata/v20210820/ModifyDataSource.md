**Example 1: 样例**



Input: 

```
tccli wedata ModifyDataSource --cli-unfold-argument  \
    --ID 1 \
    --BizParams string \
    --Category DB \
    --DatabaseName default \
    --Description desc \
    --Display test \
    --Name mysql1 \
    --Params string \
    --ClusterId string \
    --Status 1 \
    --Type CLICKHOUSE \
    --Collect string \
    --OwnerProjectId 106659848354 \
    --OwnerProjectName project1 \
    --OwnerProjectIdent pppp \
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

