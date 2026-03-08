**Example 1: 导出指定id的补丁影响的主机列表**

导出指定id的补丁影响的主机列表

Input: 

```
tccli cwp ExportPatchEffectHostList --cli-unfold-argument  \
    --KbId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "28e1cd65-0e0b-4799-9088-99e64e7b3d69",
        "TaskId": "1753945237"
    }
}
```

