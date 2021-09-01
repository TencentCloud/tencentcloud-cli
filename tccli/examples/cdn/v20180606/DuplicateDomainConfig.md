**Example 1: 拷贝参考域名的配置至新域名**



Input: 

```
tccli cdn DuplicateDomainConfig --cli-unfold-argument  \
    --Domain www.test.com \
    --ReferenceDomain reference.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "a4ac88a3-a159-47ac-9b87-19185d7deb09"
    }
}
```

