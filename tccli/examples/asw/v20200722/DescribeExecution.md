**Example 1: 查询执行详细信息**



Input: 

```
tccli asw DescribeExecution --cli-unfold-argument  \
    --ExecutionResourceName qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8
```

Output: 
```
{
    "Response": {
        "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgh9v6u1bgh9v6u2-bgh9v6u3-bgh9v6u4-bgh9v6u5",
        "Name": "bgh9v6u1bgh9v6u2-bgh9v6u3-bgh9v6u4-bgh9v6u5",
        "StartDate": "1596703766354",
        "StopDate": "0",
        "StateMachineResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8",
        "ExecutionDefinition": "{}",
        "Status": "INIT",
        "Input": "",
        "Output": "",
        "RequestId": ""
    }
}
```

