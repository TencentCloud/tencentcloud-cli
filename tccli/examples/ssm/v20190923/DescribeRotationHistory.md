**Example 1: 展示凭据轮转账号的相关信息**



Input: 

```
tccli ssm DescribeRotationHistory --cli-unfold-argument  \
    --SecretName PGSQL_remark_0714
```

Output: 
```
{
    "Response": {
        "AccountInfoList": [
            {
                "AccountName": "remm_SSM_hQ4",
                "Host": [
                    "%"
                ],
                "RotatedTime": "2026-07-14 14:21:52",
                "Version": "SSM_Current"
            }
        ],
        "TotalCount": 0,
        "VersionIDs": [],
        "RequestId": "a3ffde0c-192a-47be-8d7d-53d99fca6ebf"
    }
}
```

