**Example 1: 创建模型**



Input: 

```
tccli apis CreateModel --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --Name deepseek \
    --HttpProtocolType https \
    --TargetPath /v1 \
    --TargetHosts.0.Host 10.2.1.0 \
    --TargetHosts.0.Rank 10 \
    --CheckTargetCertsError False \
    --HttpProtocolVersion 1.1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "Model-e6866e22"
        },
        "RequestId": "8e37dddc-3e52-46c6-89dd-f510ea3c36d3"
    }
}
```

