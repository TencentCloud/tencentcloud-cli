**Example 1: 修改采样配置**

修改采样配置

Input: 

```
tccli apm ModifyApmSampleConfig --cli-unfold-argument  \
    --InstanceId apm-ewyzCXlxj \
    --SampleName testc \
    --SampleRate 100 \
    --ServiceName  \
    --OperationName 2 \
    --Status 0 \
    --Id 156 \
    --OperationType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "f678ef4b-9947-4ec0-99b8-1e6bc8b8e477"
    }
}
```

