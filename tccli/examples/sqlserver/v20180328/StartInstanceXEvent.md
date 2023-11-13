**Example 1: StartInstanceXEvent**

 开启、关闭扩展事件

Input: 

```
tccli sqlserver StartInstanceXEvent --cli-unfold-argument  \
    --InstanceId mssql-77auaua \
    --EventConfig.0.EventType blocked \
    --EventConfig.0.Threshold 0
```

Output: 
```
{
    "Response": {
        "RequestId": "AH7AAJ_909AA_AAAQ_2134343"
    }
}
```

