**Example 1: 校验域名 CNAME 配置状态**

对接入域名：test.qq.com 进行 CNAME 配置状态校验，校验的结果为 active（已正确完成 CNAME 配置），EdgeOne 为接入域名分配的指定 CNAME 域名为：test.qq.com.eo.dnse0.com。

Input: 

```
tccli teo CheckCnameStatus --cli-unfold-argument  \
    --ZoneId zone-20hyebgyfsko \
    --RecordNames example.qq.com
```

Output: 
```
{
    "Response": {
        "CnameStatus": [
            {
                "RecordName": "test.qq.com",
                "Cname": "test.qq.com.eo.dnse0.com",
                "Status": "active"
            }
        ],
        "RequestId": "d08bed0d-15bf-4d65-ab56-906aee0c845"
    }
}
```

