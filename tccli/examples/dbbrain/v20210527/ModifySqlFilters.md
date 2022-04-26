**Example 1: ModifySqlFilters**



Input: 

```
tccli dbbrain ModifySqlFilters --cli-unfold-argument  \
    --InstanceId cdb-test \
    --SessionToken cAuth \
    --FilterIds 1234 \
    --Status TERMINATED
```

Output: 
```
{
    "Response": {
        "RequestId": "b49053b9-f21c-40ec-a1ce-d1a5fae5193f"
    }
}
```

