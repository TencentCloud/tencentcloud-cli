**Example 1: 自动生成一条重定向关系**

lbl-lmeeyb1q 是一个HTTPS:443监听器，www.abc.com 是此监听器下转发规则的域名。

Input: 

```
tccli clb AutoRewrite --cli-unfold-argument  \
    --LoadBalancerId lb-r6nx1iby \
    --ListenerId lbl-lmeeyb1q \
    --Domains www.abc.com
```

Output: 
```
{
    "Response": {
        "RequestId": "e351bfdb-147a-4648-b9fe-bbcacff68789"
    }
}
```

