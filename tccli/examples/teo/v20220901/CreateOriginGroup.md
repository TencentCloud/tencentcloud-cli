**Example 1: 创建源站组**

创建HTTP专用型源站组

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-2kblak89bkx1 \
    --Name edgeone-origin \
    --Type HTTP \
    --Records.0.Record 1.1.1.1 \
    --Records.0.Type IP_DOMAIN \
    --Records.0.Weight 20 \
    --Records.1.Record s3.test.tencent.com \
    --Records.1.Type AWS_S3 \
    --Records.1.Weight 30
```

Output: 
```
{
    "Response": {
        "OriginGroupId": "origin-df19b73e-3a4c-11ee-a68f-5254000a367f",
        "RequestId": "8240f255-241c-4bae-979f-4738d7ea3f84"
    }
}
```

