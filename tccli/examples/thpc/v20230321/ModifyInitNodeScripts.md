**Example 1: 修改节点初始化脚本**

修改节点初始化脚本。

Input: 

```
tccli thpc ModifyInitNodeScripts --cli-unfold-argument  \
    --ClusterId hpc-5lyv94lq \
    --InitNodeScripts.0.ScriptPath cos://test-xxxxxxxx.cos.ap-guangzhou.myqcloud.com/test/echo.sh \
    --InitNodeScripts.0.Timeout 30
```

Output: 
```
{
    "Response": {
        "RequestId": "b40ac3ec-f0ac-4eaaa-8af8-ef2d93f37982"
    }
}
```

