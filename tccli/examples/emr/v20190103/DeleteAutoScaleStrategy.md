**Example 1: 删除弹性扩缩容规则示例**



Input: 

```
tccli emr DeleteAutoScaleStrategy --cli-unfold-argument  \
    --GroupId 6 \
    --InstanceId emr-5urm \
    --StrategyId 413 \
    --StrategyType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "586a9cb9-adcb-4f74-9e6f-01482ac4cffe"
    }
}
```

