**Example 1: 取消关联业务日志配置项和应用**



Input: 

```
tccli tsf DisassociateBusinessLogConfig --cli-unfold-argument  \
    --GroupId group-py57oeqa \
    --ConfigIdList apm-busi-log-cfg-nalzl2vq
```

Output: 
```
{
    "Response": {
        "RequestId": "027d7a35-48ca-4ce8-98de-c34e7bb4c3aa",
        "Result": true
    }
}
```

