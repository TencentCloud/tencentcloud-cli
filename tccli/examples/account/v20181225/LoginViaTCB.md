**Example 1: TCB登录云账号**



Input: 

```
tccli account LoginViaTCB --cli-unfold-argument  \
    --TmpCode xxx \
    --UserIP 119.147.10.197 \
    --UseV3Token 1 \
    --RequireStsToken 1
```

Output: 
```
{
    "Response": {
        "Token": "xxxx",
        "SecretId": "xxxx-go3KoEkGB6yFjk",
        "SecretKey": "xxxxx+Y4l0FJo1VvvY=",
        "SecretExpire": 1675423777,
        "RequestId": "238c0fb5-97f6-4d1d-b0c2-d29d42b057ca"
    }
}
```

