**Example 1: 证件核验一致示例**



Input: 

```
tccli faceid CheckIntlNameIdBirth --cli-unfold-argument  \
    --Name 张三 \
    --IdNum H00000001 \
    --BirthDate 20000101 \
    --Gender 2 \
    --ExpiryDate 20100101
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "一致",
        "RequestId": "80c7abb8-4563-4636-98c3-0499f1611a33"
    }
}
```

**Example 2: 证件核验不一致示例**



Input: 

```
tccli faceid CheckIntlNameIdBirth --cli-unfold-argument  \
    --Name 张三 \
    --IdNum H00000001 \
    --BirthDate 20000101 \
    --Gender 2 \
    --ExpiryDate 20100101
```

Output: 
```
{
    "Response": {
        "Result": "-1",
        "Description": "不一致",
        "RequestId": "80c7abb8-4563-4636-98c3-0499f1611a33"
    }
}
```

