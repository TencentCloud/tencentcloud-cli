**Example 1: 查询进程守护全局配置**

查询进程守护全局配置

Input: 

```
tccli csip DescribeProcessDaemonGlobalConf --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DisableCount": 0,
        "Enable": 0,
        "EnableCount": 0,
        "ExcludeHostCount": 0,
        "ExcludeQuuid": [],
        "IncludeHostCount": 0,
        "IncludeQuuid": [],
        "RequestId": "d40e4a6a-a269-4b06-b561-ee35dbcf727e",
        "Scope": 1
    }
}
```

