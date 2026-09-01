**Example 1: 修改集群级别**



Input: 

```
tccli cynosdb ModifyClusterLevel --cli-unfold-argument  \
    --ClusterId cynosdbmysql-6g29wqnh \
    --ClusterLevel L2
```

Output: 
```
{
    "Response": {
        "TaskId": 41854,
        "RequestId": "90e294d3-3e02-4854-bec4-cf80c39ae827"
    }
}
```

