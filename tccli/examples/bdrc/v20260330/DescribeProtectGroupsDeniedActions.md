**Example 1: 查询保护组操作掩码**



Input: 

```
tccli bdrc DescribeProtectGroupsDeniedActions --cli-unfold-argument  \
    --ProtectGroupIds pg-f9dgd2h3
```

Output: 
```
{
    "Response": {
        "ProtectGroupDeniedActionSet": [
            {
                "DeniedActions": [
                    {
                        "Action": "DeleteDrcProtectGroups",
                        "Code": "UnsupportedOperation.DisasterRecoveryProtectGroupBindResource",
                        "Message": "容灾保护组(pg-f9dgd2h3)已关联复制对，不能删除"
                    }
                ],
                "ProtectGroupId": "pg-f9dgd2h3"
            }
        ],
        "RequestId": "f0b6f67e-0036-42c4-806c-e473921868e8"
    }
}
```

