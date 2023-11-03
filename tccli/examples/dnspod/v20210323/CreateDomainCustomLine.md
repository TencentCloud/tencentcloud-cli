**Example 1: 创建域名的自定义线路**

创建域名的自定义线路

Input: 

```
tccli dnspod CreateDomainCustomLine --cli-unfold-argument  \
    --Domain dnspod.cn \
    --Name testline88 \
    --Area 6.6.6.1-6.6.6.3
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

