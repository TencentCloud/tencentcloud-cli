**Example 1: 查询GooseFS集群角色凭证**



Input: 

```
tccli goosefs DescribeClusterRoleToken --cli-unfold-argument  \
    --ClusterId g_cvm_x419f8qc \
    --RoleName test
```

Output: 
```
{
    "Response": {
        "RoleTokens": [
            {
                "RoleName": "test",
                "Token": "MTY4ODQ2NTA1NF84MzM2X2E3ZWFmMDVmLWI0MzMtNGE2Yi1iOWU2LTZiZDY5OTYwXXXXXX=="
            }
        ],
        "RequestId": "2a5ab488-0221-4315-8670-3873452be22d "
    }
}
```

