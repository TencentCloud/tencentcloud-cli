**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeCoolDownTableData --cli-unfold-argument  \
    --InstanceId str \
    --DatabaseName str
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "str",
        "List": [
            {
                "TableName": "str",
                "Size": "str",
                "RemoteSize": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

