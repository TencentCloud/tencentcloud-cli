**Example 1: 查询实例SSL状态**



Input: 

```
tccli tdmysql DescribeInstanceSSLStatus --cli-unfold-argument  \
    --InstanceId tdsql3-446540ae
```

Output: 
```
{
    "Response": {
        "SSLStatus": "Disabled",
        "RequestId": "fcdd0998-ae8a-40f4-b5c5-41d4e4496aca"
    }
}
```

