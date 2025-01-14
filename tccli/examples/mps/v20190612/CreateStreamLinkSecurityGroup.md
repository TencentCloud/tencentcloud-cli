**Example 1: 请求示例**

创建安全组。

Input: 

```
tccli mps CreateStreamLinkSecurityGroup --cli-unfold-argument  \
    --Name abc \
    --Whitelist abc
```

Output: 
```
{
    "Response": {
        "Id": "abc",
        "RequestId": "abc"
    }
}
```

