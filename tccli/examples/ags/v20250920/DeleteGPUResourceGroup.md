**Example 1: 删除空GPU资源组**

删除当前租户下已清空有效 GPU 实例、占用绑定和关联沙箱工具的资源组。

Input: 

```
tccli ags DeleteGPUResourceGroup --cli-unfold-argument  \
    --ResourceGroupId gpug-example
```

Output: 
```
{
    "Response": {
        "RequestId": "request-example"
    }
}
```

