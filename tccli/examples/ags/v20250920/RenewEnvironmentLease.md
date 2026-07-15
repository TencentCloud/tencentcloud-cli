**Example 1: 续约 EnvironmentLease**



Input: 

```
tccli ags RenewEnvironmentLease --cli-unfold-argument  \
    --EnvironmentLeaseId envl-example
```

Output: 
```
{
    "Response": {
        "EnvironmentLease": {
            "EnvironmentLeaseId": "envl-example",
            "EnvironmentId": "env-example",
            "ExpiresTime": "2026-07-03T11:01:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

