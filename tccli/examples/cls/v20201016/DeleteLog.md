**Example 1: 删除日志**



Input: 

```
tccli cls DeleteLog --cli-unfold-argument  \
    --TopicId 51586f51-****-****-9cdd-beb5e98935fd \
    --From 1784870150766 \
    --To 1884870150766 \
    --QueryString client_ip:"214.19.128.152" 
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
        "RequestId": "fbaa1635-afaa-43c2-9051-08078c3738d3"
    }
}
```

