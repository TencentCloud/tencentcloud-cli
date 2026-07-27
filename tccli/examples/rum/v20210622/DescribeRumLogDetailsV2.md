**Example 1: 调用示例**

查询日志细节

Input: 

```
tccli rum DescribeRumLogDetailsV2 --cli-unfold-argument  \
    --OrderBy asc \
    --StartTime 1767860481 \
    --Limit 100 \
    --Filter [{"Key": "id","Operator": "eq","Value": "120000"}] \
    --EndTime 1767946881 \
    --ID 120000
```

Output: 
```
{
    "Response": {
        "RequestId": "2eb407f1-108c-4fc2-9aa4-b94e72eb7e0b",
        "Result": "{\"Result\":[{\"aid\":\"5643b4b9-0000-0000-a035-0b31dd11ad1c\",\"appid\":1436000000,\"brand\":\"iPhone\",\"city\":\"xx市\",\"country\":\"中国\",\"device\":\"iPhone\"}]}"
    }
}
```

