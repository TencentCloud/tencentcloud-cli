**Example 1: 获取角色列表**



Input: 

```
tccli tdmq DescribeRoles --cli-unfold-argument  \
    --RoleName devRole \
    --Offset 0 \
    --Limit 10 \
    --ClusterId pulsar-xk3ne8k2qkp8
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "RoleSets": [
            {
                "RoleName": "test_role_3",
                "Token": "eyJzdddaWIiOiJ0ZXN0X3JvbGVfMyJ9.dbHR8m6gc4L4vZUrodhW_O9bDulZQ6lraNswNLtcUcY",
                "Remark": "devRemark",
                "CreateTime": "2020-08-04 11:59:06",
                "UpdateTime": "2020-08-04 11:59:06"
            },
            {
                "RoleName": "test_role_2",
                "Token": "eyJzdWIiOiJ0asZsXN0X3JasdvbGVfMiJ9.KTbLPg1ax2HDa51vfWmoDK5AQRmEs-_3da8yU0O61D0",
                "Remark": "devRemark",
                "CreateTime": "2020-08-03 20:23:52",
                "UpdateTime": "2020-08-03 20:23:52"
            },
            {
                "RoleName": "test_role_1",
                "Token": "eyJzddassWIiOiJ0ZXN0X3JvbGVfMSJ9.aatGv_WEZK5jqmXNX3dxQA7vWB0igKr_7eQitbweBoo",
                "Remark": "devRemark",
                "CreateTime": "2020-08-03 19:48:36",
                "UpdateTime": "2020-08-03 20:22:21"
            },
            {
                "RoleName": "test_role",
                "Token": "eyJzdWIiOiJ0ZXsasdN0X3JvbGUifQ.xeU_xkiB5wSJ8u6sUJWW",
                "Remark": "Remark1",
                "CreateTime": "2020-08-03 17:22:09",
                "UpdateTime": "2020-08-04 15:59:29"
            }
        ],
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

