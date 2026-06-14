**Example 1: 开启或关闭日志投递CLS**



Input: 

```
tccli mongodb ModifyDBInstanceLogToCLS --cli-unfold-argument  \
    --InstanceId cmgo-2gdv46zn \
    --LogType MongoDB-SlowLog \
    --Status ON \
    --Logset 64ae****-****-4e59-aba7-f60cd2264ab6 \
    --LogTopic 6a*6a*21-****-****-b612-64dad8a3c571
```

Output: 
```
{
    "Response": {
        "RequestId": "263e942e-099e-4f5d-bcab-0d87ca4eed59"
    }
}
```

