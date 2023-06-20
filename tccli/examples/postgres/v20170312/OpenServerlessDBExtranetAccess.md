**Example 1: 根据实例ID开通serverless实例外网**

根据实例ID开通serverless实例外网

Input: 

```
tccli postgres OpenServerlessDBExtranetAccess --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

**Example 2: 根据实例名开通serverless实例外网**

根据实例名开通serverless实例外网

Input: 

```
tccli postgres OpenServerlessDBExtranetAccess --cli-unfold-argument  \
    --DBInstanceName db-test
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

