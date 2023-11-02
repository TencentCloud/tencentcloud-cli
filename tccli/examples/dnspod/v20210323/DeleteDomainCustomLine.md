**Example 1: 删除域名的自定义线路**

删除域名的自定义线路

Input: 

```
tccli dnspod DeleteDomainCustomLine --cli-unfold-argument  \
    --Domain dnspod.cn \
    --Name testline88
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

