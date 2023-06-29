**Example 1: 查询节点初始化脚本信息**

查询节点初始化脚本信息。

Input: 

```
tccli thpc DescribeInitNodeScripts --cli-unfold-argument  \
    --ClusterId hpc-5lyv94lq
```

Output: 
```
{
    "Response": {
        "InitNodeScriptSet": [
            {
                "ScriptPath": "cos://test-xxxxxxxx.cos.ap-guangzhou.myqcloud.com/test/echo.sh",
                "Timeout": 30
            }
        ],
        "RequestId": "a40ac3ec-f0ac-4eee-8af8-ef2d93f37982"
    }
}
```

