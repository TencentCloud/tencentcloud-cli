**Example 1: 请求示例**



Input: 

```
tccli redis CreateInstanceAccount --cli-unfold-argument  \
    --InstanceId crs-n24q0sh7 \
    --AccountName ********test \
    --AccountPassword *********** \
    --ReadonlyPolicy master \
    --Privilege rw
```

Output: 
```
{
    "Response": {
        "TaskId": 2031374330,
        "RequestId": "1b18b553-002f-4e71-95b8-2a7293286acf"
    }
}
```

