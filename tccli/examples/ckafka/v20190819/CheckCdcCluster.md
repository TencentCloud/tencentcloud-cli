**Example 1: 查询cdc任务状态**



Input: 

```
tccli ckafka CheckCdcCluster --cli-unfold-argument  \
    --TaskId 111
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "RequestId": "20e995ed-75b9-43bb-84c0-35676567e1a8"
    }
}
```

