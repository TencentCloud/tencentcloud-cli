**Example 1: 获取告警详细信息**



Input: 

```
tccli ssa DescribeSocAlertDetails --cli-unfold-argument  \
    --AlertTimestamp 1530287122 \
    --AlertId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Detail": "1"
        },
        "RequestId": "asd-asdf-asdf-asdf-asdsfdsdsdsdsd"
    }
}
```

