**Example 1: 手机号二要素核验一致示例**



Input: 

```
tccli faceid CheckPhoneAndName --cli-unfold-argument  \
    --Mobile 16137688175 \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "验证结果一致",
        "RequestId": "368a9e91-71dc-49c7-b622-c4a300ed7370"
    }
}
```

**Example 2: 手机号二要素核验不一致示例**



Input: 

```
tccli faceid CheckPhoneAndName --cli-unfold-argument  \
    --Mobile 16137688175 \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "Description": "验证结果不一致",
        "RequestId": "eb0e4b76-4617-46f5-8582-7cc58fd20115",
        "Result": "1"
    }
}
```

