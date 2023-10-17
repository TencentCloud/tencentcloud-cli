**Example 1: 请求示例**

对主备流进行切换。

Input: 

```
tccli live SwitchBackupStream --cli-unfold-argument  \
    --PushDomainName abc \
    --AppName abc \
    --StreamName abc \
    --UpstreamSequence 843110096313761792
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

