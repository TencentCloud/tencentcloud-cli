**Example 1: 查询域名访问权限配置**

查询域名访问权限配置

Input: 

```
tccli tcb DescribeEnvAccessControl --cli-unfold-argument  \
    --EnvId c*****i**a*en*-*g*y*g**3*******
```

Output: 
```
{
    "Response": {
        "Current": [
            {
                "Action": "OPEN",
                "AuthToken": "",
                "SourceType": "PUBLIC",
                "VPCWhiteList": {
                    "Action": "",
                    "VPCs": null
                },
                "WOAAuth": ""
            }
        ],
        "RequestId": "33694abb-0e1e-4708-bcdb-db4d8dfdefe8"
    }
}
```

