**Example 1: 关闭 VPC 白名单**

关闭 VPC 白名单

Input: 

```
tccli tcb ModifyEnvAccessControl --cli-unfold-argument  \
    --EnvId co*le*i*-*ge*t***********dfee49 \
    --Sources.0.SourceType VPC \
    --Sources.0.Action OPEN \
    --Sources.0.VPCWhiteList.Action CLOSE
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
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
        "RequestId": "a57000c9-4d54-4626-9012-819801270a6b"
    }
}
```

**Example 2: 关闭公网访问**

关闭公网访问

Input: 

```
tccli tcb ModifyEnvAccessControl --cli-unfold-argument  \
    --EnvId ****e******ent-7gtyygbr36dfee49 \
    --Sources.0.SourceType PUBLIC \
    --Sources.0.Action CLOSE
```

Output: 
```
{
    "Response": {
        "AffectedRows": 2,
        "Current": [
            {
                "Action": "CLOSE",
                "AuthToken": "",
                "SourceType": "PUBLIC",
                "VPCWhiteList": {
                    "Action": "",
                    "VPCs": null
                },
                "WOAAuth": ""
            }
        ],
        "RequestId": "f44ad4d2-72c9-46a6-8cec-d951b2998159"
    }
}
```

**Example 3: 配置 VPC 白名单**

配置 VPC 白名单

Input: 

```
tccli tcb ModifyEnvAccessControl --cli-unfold-argument  \
    --EnvId ***********ent-7gtyygbr36dfee49 \
    --Sources.0.SourceType VPC \
    --Sources.0.Action OPEN \
    --Sources.0.VPCWhiteList.Action OPEN \
    --Sources.0.VPCWhiteList.VPCs.0.UniqVpcId vpc-******** \
    --Sources.0.VPCWhiteList.VPCs.0.Region ap-shanghai
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
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
        "RequestId": "92285e0b-e1db-4a40-b8bc-6bc32cd01362"
    }
}
```

