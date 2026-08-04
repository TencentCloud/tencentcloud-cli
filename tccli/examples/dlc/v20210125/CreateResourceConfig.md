**Example 1: 创建资源配置模板**



Input: 

```
tccli dlc CreateResourceConfig --cli-unfold-argument  \
    --Name test-name-01 \
    --Description test-name-description \
    --Type Ray
```

Output: 
```
{
    "Response": {
        "AppId": 260090589,
        "CreateTime": 1774340525361,
        "Description": "test-name-description",
        "Head": {
            "HighAvailability": false
        },
        "Id": "12ff2d93-5c96-4e05-98ac-be637803d381",
        "Name": "test-name-01",
        "SubAccountUin": "700002467852",
        "Type": "Ray",
        "Uin": "700002467852",
        "UpdateTime": 1774340525361,
        "RequestId": "31d6ed5e-a8ec-45ec-b41a-f34e57e52327"
    }
}
```

