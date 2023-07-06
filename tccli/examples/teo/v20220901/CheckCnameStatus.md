**Example 1: 查询域名 CNAME 状态**



Input: 

```
tccli teo CheckCnameStatus --cli-unfold-argument  \
    --RecordNames example.qq.com \
    --ZoneId zone-20hyebgyfsko
```

Output: 
```
{
    "Response": {
        "CnameStatus": [
            {
                "RecordName": "test.qq.com",
                "Cname": "test.qq.com.acc.tyxcdn.com",
                "Status": "active"
            }
        ],
        "RequestId": "d08bed0d-15bf-4d65-ab56-906aee0c845"
    }
}
```

