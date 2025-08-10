**Example 1: 修改代码仓库**



Input: 

```
tccli tione ModifyCodeRepo --cli-unfold-argument  \
    --Id test \
    --GitSecret.Secret test \
    --GitSecret.NoSecret True
```

Output: 
```
{
    "Response": {
        "RequestId": "test"
    }
}
```

