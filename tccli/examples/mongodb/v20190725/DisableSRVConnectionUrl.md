**Example 1: 关闭实例的SRV访问地址。**

关闭成功，返回任务 ID。

Input: 

```
tccli mongodb DisableSRVConnectionUrl --cli-unfold-argument  \
    --InstanceId cmgo-gnu9vvnr
```

Output: 
```
{
    "Response": {
        "FlowId": 1709799295,
        "RequestId": "763eb658-5b5a-4dff-ae17-9d86695655cd"
    }
}
```

