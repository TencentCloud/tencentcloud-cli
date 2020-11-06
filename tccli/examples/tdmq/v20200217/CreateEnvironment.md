**Example 1: 创建一个环境**



Input: 

```
tccli tdmq CreateEnvironment --cli-unfold-argument  \
    --EnvironmentId test1 \
    --MsgTTL 2000 \
    --Remark 备注
```

Output: 
```
{
    "Response": {
        "MsgTTL": 2000,
        "EnvironmentId": "test1",
        "Remark": "备注",
        "RequestId": "3f4dc986-6563-4092-aeba-4bfe8f9cbc68"
    }
}
```

