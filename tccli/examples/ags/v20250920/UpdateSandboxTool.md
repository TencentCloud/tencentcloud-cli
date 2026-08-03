**Example 1: 更新沙箱工具**



Input: 

```
tccli ags UpdateSandboxTool --cli-unfold-argument  \
    --ToolId sdt-ee4ywozw
```

Output: 
```
{
    "Response": {
        "RequestId": "12345678-1234-1234-1234-1234567890ab"
    }
}
```

**Example 2: 替换沙箱工具关联的访问策略**

完整替换沙箱工具当前关联的访问策略。

Input: 

```
tccli ags UpdateSandboxTool --cli-unfold-argument  \
    --ToolId sdt-policy123
```

Output: 
```
{
    "Response": {
        "RequestId": "req-update-tool-policy-example"
    }
}
```

**Example 3: 解除沙箱工具的全部访问策略关联**

使用空数组解除沙箱工具的全部访问策略关联。

Input: 

```
tccli ags UpdateSandboxTool --cli-unfold-argument  \
    --ToolId sdt-policy123
```

Output: 
```
{
    "Response": {
        "RequestId": "req-clear-tool-policy-example"
    }
}
```

