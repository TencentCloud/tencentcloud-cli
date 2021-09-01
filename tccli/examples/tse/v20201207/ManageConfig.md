**Example 1: 配置管理**

配置管理

Input: 

```
tccli tse ManageConfig --cli-unfold-argument  \
    --InstanceId ins-389a8c12 \
    --Type consule \
    --Command PUT \
    --Key name \
    --Value AAA
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "Result": "tom",
        "OpResult": true
    }
}
```

