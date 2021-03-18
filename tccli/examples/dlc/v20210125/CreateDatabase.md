**Example 1: demon-1**



Input: 

```
tccli dlc CreateDatabase --cli-unfold-argument  \
    --DatabaseInfo.Comment xx \
    --DatabaseInfo.Properties.0.Value xx \
    --DatabaseInfo.Properties.0.Key xx \
    --DatabaseInfo.DatabaseName xx
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "xx"
        },
        "RequestId": "xx"
    }
}
```

