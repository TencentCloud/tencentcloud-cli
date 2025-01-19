**Example 1: 续费实例postgres-apzvwncr**

包年包月实例续费操作。

Input: 

```
tccli postgres RenewInstance --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "DealName": "201806181256"
    }
}
```

