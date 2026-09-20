**Example 1: Record 更新模式：移动 stable + 新增 grey**

不提交 Source/CustomDescriptors 时是 Record 更新模式，允许 Description/LabelMutations。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

**Example 2: Version 创建模式：MCP URL_IMPORT**

提交内容输入进入 Version 创建模式；禁止同时提交 Description/LabelMutations。

Input: 

```
tccli ags UpdateRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

