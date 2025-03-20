**Example 1: 查询木马自动隔离设置**

查询木马自动隔离设置

Input: 

```
tccli tcss DescribeVirusAutoIsolateSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AutoIsolateSwitch": true,
        "IsKillProgress": true,
        "UserAutoIsolateKillSwitch": true,
        "RequestId": "F00A8503-6233-452E-913E-DAFE9******"
    }
}
```

