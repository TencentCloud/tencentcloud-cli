**Example 1: 查询创建者手机号码下的所有机构**

查询创建者手机号码下的所有机构

Input: 

```
tccli ocl DescribeOrg --cli-unfold-argument  \
    --Phone 13688888888
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "OrgName": "whoami"
            },
            {
                "OrgName": "whoami11"
            }
        ],
        "RequestId": "ddgdgaadfgddfa"
    }
}
```

