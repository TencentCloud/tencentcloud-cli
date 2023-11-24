**Example 1: 查询版本发布环境列表**

查询站点 ID 为 zone-2k3lomh6sdcb 的站点的环境列表信息。

Input: 

```
tccli teo DescribeEnvironments --cli-unfold-argument  \
    --ZoneId zone-2k3lomh6sdcb
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvInfos": [
            {
                "EnvId": "env-2kplomhisdcb",
                "EnvType": "production",
                "Status": "running",
                "Scope": [
                    "ALL"
                ],
                "CreateTime": "2023-09-21T00:00:00+00:00",
                "UpdateTime": "2023-09-22T00:00:00+00:00",
                "CurrentConfigGroupVersionInfos": [
                    {
                        "VersionId": "ver-2k3lomh6sdcb",
                        "VersionNumber": "1.0",
                        "GroupId": "cg-2k3lomh6sdcb",
                        "GroupType": "l7_acceleration",
                        "Description": "用于生产",
                        "Status": "active",
                        "CreateTime": "2023-09-22T00:00:00+00:00"
                    }
                ]
            }
        ],
        "RequestId": "9bd9c732-0f9a-4cd3-a3e8-1e9db5e53631"
    }
}
```

