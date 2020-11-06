**Example 1: Getting credentials required for instance login**

This example shows you how to get the credentials required for instance login.

Input: 

```
tccli gse GetInstanceAccess --cli-unfold-argument  \
    --FleetId xxx \
    --InstanceId xxx
```

Output: 
```
{
    "InstanceAccess": {
        "Credentials": {
            "Secret": "xxxxx",
            "UserName": "xxxxx"
        },
        "FleetId": "xxxx",
        "InstanceId": "xxxx",
        "IpAddress": "xxxxx",
        "OperatingSystem": "xxxxx",
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

