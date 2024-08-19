**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeCoolDownTableData --cli-unfold-argument  \
    --InstanceId abc \
    --DatabaseName abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "List": [
            {
                "TableName": "abc",
                "Size": "abc",
                "RemoteSize": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

