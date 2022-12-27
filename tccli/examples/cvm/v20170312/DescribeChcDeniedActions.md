**Example 1: 查询CHC物理服务器禁止做的操作**

查询CHC物理服务器禁止做的操作

Input: 

```
tccli cvm DescribeChcDeniedActions --cli-unfold-argument  \
    --ChcIds chc-adf34aft chc-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "ChcHostDeniedActionSet": [
            {
                "ChcId": "chc-1a2b3c4d",
                "DenyActions": [
                    "ConfigureChcAssistVpc",
                    "RunInstances"
                ],
                "State": "INIT"
            },
            {
                "ChcId": "chc-adf34aft",
                "DenyActions": [
                    "ConfigureChcAssistVpc",
                    "RunInstances"
                ],
                "State": "INIT"
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

