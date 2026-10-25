**Example 1: DescribeFieldValues示例**



Input: 

```
tccli rum DescribeFieldValues --cli-unfold-argument  \
    --AppId 146662 \
    --StartTime 123 \
    --EndTime 3545 \
    --FieldName app_version \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": "{\"Total\":0,\"Values\":[]}",
        "RequestId": "5493d519-23b0-4c53-bf70-43404dc71b8d"
    }
}
```

