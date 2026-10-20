**Example 1: 查询账号列表**

查询账号列表

Input: 

```
tccli cdb DescribeAccounts --cli-unfold-argument  \
    --InstanceId cdb-mw6uxcyt
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2026-08-27 10:14:08",
                "Host": "%",
                "MaxUserConnections": 0,
                "ModifyPasswordTime": "2026-08-27 19:18:07",
                "ModifyTime": "2026-08-27 19:18:07",
                "Notes": "",
                "OpenCam": false,
                "User": "root"
            },
            {
                "CreateTime": "2026-08-27 19:18:36",
                "Host": "%",
                "MaxUserConnections": 0,
                "ModifyPasswordTime": "2026-08-27 19:18:36",
                "ModifyTime": "2026-08-27 19:18:36",
                "Notes": "",
                "OpenCam": false,
                "User": "testqqq"
            }
        ],
        "MaxUserConnections": 10240,
        "RequestId": "527dcdb8-9c9b-4fb0-9e47-e8316737e051",
        "TotalCount": 2
    }
}
```

