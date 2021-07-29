**Example 1: 查询license信息接口**



Input: 

```
tccli wav QueryLicenseInfo --cli-unfold-argument  \
    --License A1c0tVAAAGSB1
```

Output: 
```
{
    "Response": {
        "LicenseInfo": {
            "DestroyTime": "2022-07-15 00:00:00",
            "ResourceEndTime": "2022-07-01 00:00:00",
            "Extra": "",
            "IsolationDeadline": "2022-07-08 00:00:00",
            "License": "A1c0tVAAAGSB1",
            "LicenseEdition": 1,
            "ResourceStartTime": "2021-07-01 00:00:00",
            "Status": 1
        },
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

