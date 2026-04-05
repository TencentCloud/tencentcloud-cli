**Example 1: demo**



Input: 

```
tccli wedata GetInfraCosTMPToken --cli-unfold-argument  \
    --InfraType connection
```

Output: 
```
{
    "Response": {
        "Data": {
            "CosBucket": "XXXXX",
            "CosRegion": "region",
            "ExpiredTime": "1766574922",
            "Path": "/connection/XXXXX/XXXXX",
            "RoleOwnerUin": "",
            "SecretId": "XXXXX",
            "SecretKey": "XXXXX=",
            "Token": "XXXXX"
        },
        "RequestId": "c746e21b-598e-47b2-bd17-69721575f57b"
    }
}
```

