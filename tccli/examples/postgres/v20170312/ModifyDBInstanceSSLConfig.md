**Example 1: 关闭SSL**

关闭实例SSL

Input: 

```
tccli postgres ModifyDBInstanceSSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-5gevh7gr \
    --SSLEnabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "5878440a-028f-4fe4-8786-240665d0105e",
        "TaskId": 100015
    }
}
```

**Example 2: 开启SSL**

开启实例SSL，并设置保护地址为实例内网地址

Input: 

```
tccli postgres ModifyDBInstanceSSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-5gevh7gr \
    --SSLEnabled True \
    --ConnectAddress 10.6.0.4
```

Output: 
```
{
    "Response": {
        "RequestId": "e39921c1-2d50-4c55-8bca-8bdff0a387e8",
        "TaskId": 100016
    }
}
```

