**Example 1: 查询环境变量**



Input: 

```
tccli wedata GetAppEnvs --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppKey 07fb16d517745134000392296d3db
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppKey": "07fb16d517745134000392296d3db",
            "DeployKey": "1efa4ae21774513417497c28944a0",
            "EnvVars": "{\"WEDATA_REGION\":\"ap-guangzhou\"}"
        },
        "RequestId": "08a81ec9-1ab6-4dee-ba37-f7054730df41"
    }
}
```

