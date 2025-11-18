**Example 1: test**

修改apm业务系统与其他产品的关联关系

Input: 

```
tccli apm ModifyApmAssociation --cli-unfold-argument  \
    --ProductName Prometheus \
    --Status 2 \
    --InstanceId apm-059oXBfTL \
    --PeerId prom-26july28
```

Output: 
```
{
    "Response": {
        "RequestId": "9f3e2957-bdf4-4485-98fa-fd7119ec6800"
    }
}
```

