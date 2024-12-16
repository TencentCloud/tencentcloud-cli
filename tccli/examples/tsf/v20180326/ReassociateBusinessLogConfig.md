**Example 1: 重关联业务日志配置**



Input: 

```
tccli tsf ReassociateBusinessLogConfig --cli-unfold-argument  \
    --ApplicationId application-6a79x94v \
    --GroupId group-6a79x94v \
    --ConfigId config-old \
    --NewConfigId config-new
```

Output: 
```
{
    "Response": {
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

