**Example 1: 1**



Input: 

```
tccli tdmysql ModifyUserPrivileges --cli-unfold-argument  \
    --InstanceId tdsql3-0b2f04e0 \
    --Users.0.UserName mysql.sys \
    --Users.0.Host localhost \
    --GlobalPrivileges SELECT
```

Output: 
```
{
    "Response": {
        "RequestId": "4c2c4b96-5807-4c63-b55c-78a93937d111"
    }
}
```

