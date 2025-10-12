**Example 1: 删除血缘**

删除血缘

Input: 

```
tccli wedata DeleteLineage --cli-unfold-argument  \
    --Relations.0.Source.Description DORIS \
    --Relations.0.Source.Platform WEDATA \
    --Relations.0.Source.ResourceType TABLE \
    --Relations.0.Target.Description DORIS \
    --Relations.0.Target.Platform WEDATA \
    --Relations.0.Target.ResourceType TABLE \
    --Relations.0.Processes.0.Platform WEDATA \
    --Relations.0.Processes.0.ProcessId third_::other::Task-02 \
    --Relations.0.Processes.0.ProcessType THIRD_REPORT
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 1
        },
        "RequestId": "RequestId"
    }
}
```

