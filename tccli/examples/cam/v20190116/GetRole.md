**Example 1: 获取角色详情**



Input: 

```
tccli cam GetRole --cli-unfold-argument  \
    --RoleId 4611686018427844696
```

Output: 
```
{
    "Response": {
        "RoleInfo": {
            "RoleId": "4611686018427844696",
            "RoleName": "test_1234544",
            "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}",
            "Description": "abc",
            "AddTime": "2019-07-10 11:22:27",
            "UpdateTime": "2019-07-10 11:22:27",
            "ConsoleLogin": 0,
            "RoleType": "system",
            "SessionDuration": 43200,
            "DeletionTaskId": "114",
            "Tags": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ]
        },
        "RequestId": "87fb9770-0fca-4c5a-b985-1c36b05a95cb"
    }
}
```

**Example 2: 获取服务相关角色详情**



Input: 

```
tccli cam GetRole --cli-unfold-argument  \
    --RoleId 4611686018427411642
```

Output: 
```
{
    "Response": {
        "RoleInfo": {
            "RoleId": "4611686018427411642",
            "RoleName": "byron3214_QcsRole",
            "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"ccslinked.qcloud.com\"]}}]}",
            "Description": "role222",
            "AddTime": "2020-03-25 11:03:00",
            "UpdateTime": "2020-03-25 11:03:00",
            "ConsoleLogin": 0,
            "RoleType": "service_linked",
            "SessionDuration": 43200,
            "DeletionTaskId": "114",
            "Tags": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ]
        },
        "RequestId": "1fb826eb-6d21-42f3-8f6e-9f51360f585d"
    }
}
```

