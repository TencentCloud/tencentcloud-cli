**Example 1: 创建 web 播放器基础版**

web播发器需要签发license，这里可以创建基础版license

Input: 

```
tccli vcube CreateApplicationAndWebPlayerLicense --cli-unfold-argument  \
    --AppName 我的应用 \
    --DomainList abc.com ddd.cn
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

