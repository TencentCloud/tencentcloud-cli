**Example 1: 删除运行任务标签成功**



Input: 

```
tccli wedata DeleteTrainingTaskTag --cli-unfold-argument  \
    --WorkspaceId 10086 \
    --RunId 1 \
    --Key key1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "5908d5f4-a790-4e9b-a2ae-936b4d8d91ae"
    }
}
```

