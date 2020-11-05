**Example 1: Disabling public network access for TencentDB instance**



Input: 

```
tccli mariadb CloseDBExtranetAccess --cli-unfold-argument  \
    --InstanceId tdsql-avw0207d
```

Output: 
```
{
    "Response": {
        "RequestId": "2d1e21a2-b29a-490a-8be0-b61287d92e28",
        "FlowId": 3324
    }
}
```

