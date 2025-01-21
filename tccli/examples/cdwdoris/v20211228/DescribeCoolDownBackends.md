**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeCoolDownBackends --cli-unfold-argument  \
    --InstanceId str
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "str",
        "List": [
            {
                "Host": "str",
                "DataUsedCapacity": "str",
                "TotalCapacity": "str",
                "RemoteUsedCapacity": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

