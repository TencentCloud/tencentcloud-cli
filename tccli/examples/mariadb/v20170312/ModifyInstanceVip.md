**Example 1: 修改实例VIP**



Input: 

```
tccli mariadb ModifyInstanceVip --cli-unfold-argument  \
    --InstanceId tdsql-jv8z8fhl \
    --VipReleaseDelay 168 \
    --Vip 10.0.0.2
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "FlowId": 1122
    }
}
```

