**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeCoolDownBackends --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "List": [
            {
                "Host": "abc",
                "DataUsedCapacity": "abc",
                "TotalCapacity": "abc",
                "RemoteUsedCapacity": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

