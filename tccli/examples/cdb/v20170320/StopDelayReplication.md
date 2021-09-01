**Example 1: 停止延迟复制**

停止延迟只读实例的延迟复制。

Input: 

```
tccli cdb StopDelayReplication --cli-unfold-argument  \
    --InstanceId cdbro-test
```

Output: 
```
{
    "Response": {
        "RequestId": "28a67cf3-4589-8534-2be0-17475fa5c892"
    }
}
```

