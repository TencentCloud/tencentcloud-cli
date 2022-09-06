**Example 1: 授权腾讯云用户**

Grafana实例授权其他腾讯云用户

Input: 

```
tccli monitor CreateSSOAccount --cli-unfold-argument  \
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
        "UserId": "xx",
        "RequestId": "xx"
    }
}
```

