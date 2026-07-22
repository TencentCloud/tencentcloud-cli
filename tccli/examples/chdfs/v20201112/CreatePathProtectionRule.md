**Example 1: 创建路径保护规则**

创建路径保护规则

Input: 

```
tccli chdfs CreatePathProtectionRule --cli-unfold-argument  \
    --Status 1 \
    --Path /protect \
    --FileSystemId f4mhaqkciq0 \
    --Name test
```

Output: 
```
{
    "Response": {
        "RequestId": "5d6d3ef8-db1d-40de-afa1-d340302458bb"
    }
}
```

