**Example 1: 更改审计服务配置**

修改审计日志保存周期

Input: 

```
tccli mongodb ModifyAuditService --cli-unfold-argument  \
    --LogExpireDay 365 \
    --InstanceId cmgo-xfts****
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

