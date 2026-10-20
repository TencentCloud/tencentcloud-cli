**Example 1: 成功示例**



Input: 

```
tccli adp DescribeNodeBatchRun --cli-unfold-argument  \
    --AppId 2046434807234765632 \
    --Index 3 \
    --NodeId ed5fc56d-224c-387c-ee3f-427fa60bcb48 \
    --WorkflowRunId wfr-c928613c-cb3f-4c49-bbc6-83f862067e7f
```

Output: 
```
{
    "Response": {
        "FailCode": "",
        "FailMessage": "",
        "Input": "{\"age\":3,\"name\":\"hhh\"}",
        "InputRef": "",
        "Output": "{\"age\":3,\"name\":\"hhh\"}",
        "OutputRef": "",
        "Status": 3,
        "RequestId": "9f9d3dc1-ecb3-41de-8a6a-f9ee011d635b"
    }
}
```

