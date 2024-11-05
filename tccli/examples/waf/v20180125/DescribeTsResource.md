**Example 1: 查询示例**



Input: 

```
tccli waf DescribeTsResource --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values 010000000 \
    --Filters.0.Name v1 \
    --Filters.0.ExactMatch False \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "Status": 1,
                "Ip": "1.1.1.1",
                "Auth": "skey-auth",
                "Id": 1,
                "SubRegion": "gz-sub-1",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "Port": 1,
                "Type": "pub",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "uuid-wwe-qqji-38iw"
    }
}
```

