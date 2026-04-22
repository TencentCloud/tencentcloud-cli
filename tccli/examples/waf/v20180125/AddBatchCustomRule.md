**Example 1: 批量新增自定义规则接口**



Input: 

```
tccli waf AddBatchCustomRule --cli-unfold-argument  \
    --Name name \
    --ExpireTime 0 \
    --SortId 0 \
    --ActionType 1 \
    --Redirect /redirect \
    --Bypass cc \
    --Remark remark \
    --EventId 11101 \
    --Domains www.test.com \
    --Strategies.0.Field URL \
    --Strategies.0.Arg  \
    --Strategies.0.CompareFunc eq \
    --Strategies.0.Content /acl
```

Output: 
```
{
    "Response": {
        "Res": "success",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

