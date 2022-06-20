**Example 1: 重关联业务日志配置**



Input: 

```
tccli tsf ReassociateBusinessLogConfig --cli-unfold-argument  \
    --ApplicationId test \
    --GroupId test \
    --ConfigId config-old \
    --NewConfigId config-new
```

Output: 
```
{
    "Response": {
        "RequestId": "!2vko3112424d2322"
    }
}
```

