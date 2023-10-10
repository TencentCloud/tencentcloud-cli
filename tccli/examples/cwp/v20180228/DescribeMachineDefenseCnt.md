**Example 1: 查询主机高级防御事件数统计**

查询主机高级防御事件数统计

Input: 

```
tccli cwp DescribeMachineDefenseCnt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FileTamper": 1,
        "RequestId": " 0aafcd71-9603-4a8c-88c3-2d567a7143e8 ",
        "AttackLogs": 1
    }
}
```

