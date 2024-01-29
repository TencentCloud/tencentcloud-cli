**Example 1: 开启或关闭CDB日志投递CLS**

CDB实例慢日志、错误日志投递到CLS

Input: 

```
tccli cdb ModifyDBInstanceLogToCLS --cli-unfold-argument  \
    --InstanceId cdb-ewa3b \
    --LogType error \
    --Status ON \
    --CreateLogset True \
    --Logset sub_fyrtjbqw \
    --CreateLogTopic True \
    --LogTopic my_test \
    --Period 1 \
    --CreateIndex True
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

