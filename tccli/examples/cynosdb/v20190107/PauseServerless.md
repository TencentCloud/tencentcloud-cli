**Example 1: 暂停serverless集群**



Input: 

```
tccli cynosdb PauseServerless --cli-unfold-argument  \
    --ClusterId cynosdbmysql-8vcxoq75 \
    --ForcePause 1
```

Output: 
```
{
    "Response": {
        "FlowId": 1008306,
        "RequestId": "37508f2e-23eb-11eb-a713-525400b7dd5a"
    }
}
```

