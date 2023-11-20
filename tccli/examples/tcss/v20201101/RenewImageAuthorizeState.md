**Example 1: 授权镜像扫描**



Input: 

```
tccli tcss RenewImageAuthorizeState --cli-unfold-argument  \
    --AllImages false \
    --ImageIds aaa
```

Output: 
```
{
    "Response": {
        "RequestId": "aaa"
    }
}
```

