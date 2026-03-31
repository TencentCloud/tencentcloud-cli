**Example 1: 获取个人运行环境网络信息**

获取个人运行环境网络信息

Input: 

```
tccli wedata GetCodeWorkspaceNetworkInfo --cli-unfold-argument  \
    --CodeWorkspaceId a6e995ef-94ad-4516-91f3-5c7c85f9cf19
```

Output: 
```
{
    "Response": {
        "Data": {
            "CsInnerPort": 8080,
            "CsVIp": "21.78.37.192",
            "CsVPort": 8080,
            "GatewayIp": "",
            "GatewayPort": 0,
            "InnerIp": "192.168.7.50",
            "JsInnerPort": 8889,
            "JsVIp": "21.78.37.192",
            "JsVPort": 8889,
            "MsInnerPort": 3000,
            "MsVIp": "21.78.37.192",
            "MsVPort": 3000
        },
        "RequestId": "44844e27-fe85-4198-ba7c-75e710eb0f51"
    }
}
```

