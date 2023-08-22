**Example 1: 接口调用示例**

接口调用示例

Input: 

```
tccli scf UpdateTrigger --cli-unfold-argument  \
    --Enable CLOSE \
    --FunctionName helloworld-xxxxxxxx \
    --TriggerName 	
SCF-timer-xxxxxxxx \
    --Type timer \
    --Qualifier $DEFAULT \
    --Namespace default \
    --TriggerDesc 0 0 0 */2 * * * \
    --Description 测试 \
    --CustomArgument 中文测试
```

Output: 
```
{
    "Response": {
        "RequestId": "375d4028-xxxx-xxxxf-xxxx-2331cb974fc3"
    }
}
```

