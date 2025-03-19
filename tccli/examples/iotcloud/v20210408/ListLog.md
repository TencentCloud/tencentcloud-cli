**Example 1: 查询日志示例**



Input: 

```
tccli iotcloud ListLog --cli-unfold-argument  \
    --MinTime 1530244265000 \
    --MaxTime 1530258665000 \
    --Keywords UTY6QRLMQY \
    --Context hello \
    --MaxNum 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "Invalid arguments[Keywords]"
        },
        "RequestId": "10059673-305d-4201-9b30-59bf3eb397ef"
    }
}
```

