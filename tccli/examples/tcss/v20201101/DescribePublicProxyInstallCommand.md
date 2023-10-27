**Example 1: 查询公共代理命令**



Input: 

```
tccli tcss DescribePublicProxyInstallCommand --cli-unfold-argument  \
    --IP abc
```

Output: 
```
{
    "Response": {
        "KeepAliveCommand": "abc",
        "NginxCommand": "abc",
        "RequestId": "abc"
    }
}
```

