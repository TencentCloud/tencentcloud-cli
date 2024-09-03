**Example 1: ResetConcurrentPackages示例**

重置并发包，断开所有用户连接

Input: 

```
tccli car ResetConcurrentPackages --cli-unfold-argument  \
    --ConcurrentPackageIds cac-1234abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

