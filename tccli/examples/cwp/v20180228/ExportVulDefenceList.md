**Example 1: 示例**



Input: 

```
tccli cwp ExportVulDefenceList --cli-unfold-argument  \
    --Where Uuid \
    --Filters.0.Values 625e4ed2-f91a-4b35-afdb-98a6216ef722 \
    --Filters.0.Name Uuid \
    --Filters.0.ExactMatch false
```

Output: 
```
{
    "Response": {
        "RequestId": "d14c8764-de8d-4eda-89e9-3a4b4fb5d7c4",
        "TaskId": "1730637975165420573"
    }
}
```

