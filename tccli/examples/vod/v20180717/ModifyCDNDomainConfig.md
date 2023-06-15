**Example 1: 修改域名源站**

修改域名源站

Input: 

```
tccli vod ModifyCDNDomainConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --Config.Origin.Origins src2.myexample.com \
    --Config.Origin.OriginType domain
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

