**Example 1: 范例**



Input: 

```
tccli wedata CreateTask --cli-unfold-argument  \
    --ProjectId 1 \
    --WorkflowId 34e51bc4-0cd9-11ed-8909-bc97e105ba60 \
    --TaskExt.0.Key aa \
    --TaskExt.0.Value vv \
    --TaskName aaab \
    --TaskType 35
```

Output: 
```
{
    "Response": {
        "RequestId": "2eeae735-b9c1-4c99-a4dd-54f3e8da674f",
        "Data": {
            "Id": "20220801203612642"
        }
    }
}
```

