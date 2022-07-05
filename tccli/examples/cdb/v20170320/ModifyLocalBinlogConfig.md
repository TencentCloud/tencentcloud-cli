**Example 1: 修改本地binlog保留策略**



Input: 

```
tccli cdb ModifyLocalBinlogConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --MaxUsage 30 \
    --SaveHours 72
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

