**Example 1: 开通审计**



Input: 

```
tccli cynosdb OpenAuditService --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-6990cckk \
    --LogExpireDay 30 \
    --HighLogExpireDay 7
```

Output: 
```
{
    "Response": {
        "RequestId": "43-12121-812w1221213-62usf9093"
    }
}
```

