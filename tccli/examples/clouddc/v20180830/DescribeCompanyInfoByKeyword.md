**Example 1: 示例**



Input: 

```
tccli clouddc DescribeCompanyInfoByKeyword --cli-unfold-argument  \
    --Keyword 拼多多 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "JsonString": "{\"corporations\":[{\"Eid\":\"9088b55b-7217-40b4-9bd7-9719fe347b81\",\"Name\":\"\\u4e0a\\u6d77\\u5bfb\\u68a6\\u4fe1\\u606f\\u6280\\u672f\\u6709\\u9650\\u516c\\u53f8\",\"SearchName\":\"\\u62fc\\u591a\\u591a\",\"SearchNameType\":\"product\"}]}",
        "RequestId": "96ce0214-d3f1-41e2-9bd3-26d687a90ebc"
    }
}
```

