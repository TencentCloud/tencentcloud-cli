**Example 1: 修改触发器状态**



Input: 

```
tccli scf UpdateTriggerStatus --cli-unfold-argument  \
    --Enable CLOSE \
    --Type timer \
    --FunctionName <FunctionName> \
    --TriggerName <TriggerName>
```

Output: 
```
{
    "Response": {
        "RequestId": "375d4028-2666-4cef-bcab-2331cb974fc3"
    }
}
```

