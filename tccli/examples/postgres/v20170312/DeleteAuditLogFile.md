**Example 1: 删除审计日志文件**

删除审计日志文件

Input: 

```
tccli postgres DeleteAuditLogFile --cli-unfold-argument  \
    --InstanceId postgres-nqg1hcnj \
    --Product postgres \
    --FileName 1253431691_postgres-nqg1hcnj_1774420264_151841011.csv
```

Output: 
```
{
    "Response": {
        "RequestId": "21d1eaaa-32cc-46ee-8568-eef4f615d559"
    }
}
```

