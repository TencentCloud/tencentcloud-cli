**Example 1: 修改日志**



Input: 

```
tccli cls ModifyLog --cli-unfold-argument  \
    --TopicId 51586f51-****-****-9cdd-beb5e98935fd \
    --From 1784870150766 \
    --To 1784879583478 \
    --QueryString client_ip:"***.249.***.109" \
    --ModifyMode REPLACE \
    --ModifyContent {"bytes_sent":222222,"client_ip":"110.***.***.109"}
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
        "RequestId": "a3979497-852f-499e-88b4-7763e4fcfd3d"
    }
}
```

