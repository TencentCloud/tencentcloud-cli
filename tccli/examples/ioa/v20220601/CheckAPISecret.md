**Example 1: 密钥检查**

检查密钥名称是否重复

Input: 

```
tccli ioa CheckAPISecret --cli-unfold-argument  \
    --Title abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsExist": 0
        },
        "RequestId": "abc"
    }
}
```

