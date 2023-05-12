**Example 1: 获取可运行时列表**

返回用户可用的运行时列表，发布应用时返回的运行时环境，仅shared和standalone运行时，无sandbox运行时，并且只有running状态的

Input: 

```
tccli eis ListDeployableRuntimesMC --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Runtimes": [
            {
                "RuntimeId": 0,
                "DisplayName": "abc",
                "Type": 0,
                "Zone": "abc",
                "Area": "abc",
                "Addr": "abc",
                "Status": 0,
                "ExpiredAt": 0,
                "RuntimeClass": 0,
                "Deployed": true
            }
        ],
        "RequestId": "abc"
    }
}
```

