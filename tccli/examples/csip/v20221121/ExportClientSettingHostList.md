**Example 1: 导出防卸载主机配置列表**

导出防卸载主机配置列表

Input: 

```
tccli csip ExportClientSettingHostList --cli-unfold-argument  \
    --BusiType PreventUninstall
```

Output: 
```
{
    "Response": {
        "RequestId": "02e39774-629a-46cc-bda6-c5e5fa667f3d",
        "TaskId": "1749804412"
    }
}
```

