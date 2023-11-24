**Example 1: 查询版本发布历史**

查询站点 ID 为 zone-3swlomhssdcb 下环境 ID 为 env-2kpeomhisdwb 的版本发布历史。

Input: 

```
tccli teo DescribeDeployHistory --cli-unfold-argument  \
    --ZoneId zone-3swlomhssdcb \
    --EnvId env-2kpeomhisdwb
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Records": [
            {
                "ConfigGroupVersionInfos": [
                    {
                        "VersionId": "ver-2kplomhiqdcb",
                        "VersionNumber": "1.0",
                        "GroupId": "cg-2kplomhisdcb",
                        "GroupType": "l7_acceleration",
                        "Description": "测试版本",
                        "Status": "active",
                        "CreateTime": "2020-09-22T00:00:00+00:00"
                    }
                ],
                "RecordId": "dr-2nvehs3fa40u",
                "DeployTime": "2023-09-22T00:00:00+00:00",
                "Status": "success",
                "Message": "发布成功"
            }
        ],
        "RequestId": "9bd9c732-8f9a-4cd3-a3e0-1c2db5e53631"
    }
}
```

