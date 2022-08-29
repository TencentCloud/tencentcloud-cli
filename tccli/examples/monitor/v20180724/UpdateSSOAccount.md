**Example 1: 更新账号信息**

更新权限和备注

Input: 

```
tccli monitor UpdateSSOAccount --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --UserId 100000000 \
    --Role.0.Organization Org \
    --Role.0.Role Admin \
    --Notes 授权该用户
```

Output: 
```
{
    "Response": {
        "RequestId": "qmunlpf51noe13qp5vyvg7mq5t4t4w6u"
    }
}
```

