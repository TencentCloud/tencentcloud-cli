**Example 1: 查询日志示例**



Input: 

```
tccli iotcloud ListLog --cli-unfold-argument  \
    --MinTime 1530244265000 \
    --MaxTime 1530258665000 \
    --Keywords abc
```

Output: 
```
{
    "Response": {
        "Context": "",
        "Listover": false,
        "TotalCount": 0,
        "Results": [
            {
                "Content": "Device disconnect,connect time:2018-05-24 14:59:45,last avtive time:2018-05-24 14:59:45",
                "DeviceName": "test",
                "ProductId": "ABCDE12345",
                "RequestId": "17431401761688125443",
                "Result": "SUCC",
                "Scene": "STATUS",
                "Time": "2018-05-24 15:00:04.725",
                "Userid": "100000005194"
            }
        ],
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

