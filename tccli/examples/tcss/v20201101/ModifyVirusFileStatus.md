**Example 1: 运行时更新木马文件事件状态**



Input: 

```
tccli tcss ModifyVirusFileStatus --cli-unfold-argument  \
    --EventIdSet xx \
    --Status xx \
    --Remark xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

