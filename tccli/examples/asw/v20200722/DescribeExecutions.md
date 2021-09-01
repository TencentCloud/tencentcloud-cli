**Example 1: 状态机执行列表**



Input: 

```
tccli asw DescribeExecutions --cli-unfold-argument  \
    --StateMachineResourceName qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8 \
    --PageSize 100 \
    --PageIndex 1 \
    --FilterExecutionStatus INIT
```

Output: 
```
{
    "Response": {
        "RequestId": ""
    }
}
```

