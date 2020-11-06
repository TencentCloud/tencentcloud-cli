**Example 1: 删除一个集群中的模型**



Input: 

```
tccli tia DeleteModel --cli-unfold-argument  \
    --Name test-model \
    --Cluster ap-beijing
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

**Example 2: 删除一个SCF模型**



Input: 

```
tccli tia DeleteModel --cli-unfold-argument  \
    --Name test-model \
    --ServType serverless
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

