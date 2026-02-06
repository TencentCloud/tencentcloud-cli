**Example 1: 查询用户所有账号信息**



Input: 

```
tccli cdb DescribeAccounts --cli-unfold-argument  \
    --InstanceId cdb-b1airfvv
```

Output: 
```
{
    "Response": {
        "RequestId": "507f6863-2827-4c2c-9c3b-fbbcc32e1ed4",
        "Items": [
            {
                "CreateTime": "2025-09-04 14:56:31",
                "Host": "%",
                "MaxUserConnections": 0,
                "ModifyPasswordTime": "2025-09-04 14:56:31",
                "ModifyTime": "2025-09-04 14:59:10",
                "Notes": "",
                "OpenCam": false,
                "User": "ching"
            },
            {
                "CreateTime": "2025-09-02 16:18:42",
                "Host": "%",
                "MaxUserConnections": 0,
                "ModifyPasswordTime": "2025-09-02 16:18:42",
                "ModifyTime": "2025-09-02 16:18:42",
                "Notes": "",
                "OpenCam": false,
                "User": "root"
            }
        ],
        "MaxUserConnections": 10240,
        "TotalCount": 2
    }
}
```

