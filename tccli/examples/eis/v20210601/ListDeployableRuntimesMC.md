**Example 1: 获取可部署运行时列表**

返回用户可用的运行时列表，发布应用时返回的运行时环境，仅shared和standalone运行时，无sandbox运行时，并且只有running状态的

Input: 

```
tccli eis ListDeployableRuntimesMC --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Runtimes": [
            {
                "DisplayName": "xx",
                "Zone": "xx",
                "Type": 2,
                "RuntimeId": 123,
                "Area": "zz",
                "Addr": "ipaas.tianjin.com"
            }
        ]
    }
}
```

