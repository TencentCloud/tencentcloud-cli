**Example 1: 检查联通性**



Input: 

```
tccli sqlserver ExecuteDBBrainQuery --cli-unfold-argument  \
    --InstanceId mssql-0ma5rgjx \
    --SqlNo 1 \
    --NodeRole master
```

Output: 
```
{
    "Response": {
        "Data": [
            "{\"Ok\":1}"
        ],
        "Message": "success",
        "Names": [
            "Ok"
        ],
        "RequestId": "9d217578-7e3a-4cc0-a9cd-b1a6501b45d6"
    }
}
```

