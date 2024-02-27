**Example 1: 删除弹性扩缩容规则示例**



Input: 

```
tccli emr DeleteAutoScaleStrategy --cli-unfold-argument  \
    --InstanceId emr-3ap64zl6 \
    --StrategyType 1 \
    --StrategyId 42
```

Output: 
```
{
    "Response": {
        "RequestId": "0bef5627-4e40-4245-ba9c-2a83517b6880"
    }
}
```

