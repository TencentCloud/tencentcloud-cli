**Example 1: 修改数据库账号描述**



Input: 

```
tccli tdcpg ModifyAccountDescription --cli-unfold-argument  \
    --ClusterId tdcpg-xxx \
    --AccountName root \
    --AccountDescription 我的账号
```

Output: 
```
{
    "Response": {
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

