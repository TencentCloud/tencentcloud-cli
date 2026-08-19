**Example 1: 查询防卸载配置**

查询防卸载配置

Input: 

```
tccli csip DescribePreventUninstallGlobalConf --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Enable": 1,
        "ExcludeHostCount": 0,
        "ExcludeQuuid": [],
        "IncludeHostCount": 156,
        "IncludeQuuid": [],
        "RequestId": "58112d39-777d-4c2f-a7bb-609f6012ad53",
        "EnableCount": 10,
        "DisableCount": 0,
        "Scope": 1
    }
}
```

