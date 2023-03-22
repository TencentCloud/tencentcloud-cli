**Example 1: 查询所有监控类型**

查询所有监控类型

Input: 

```
tccli monitor DescribeMonitorTypes --cli-unfold-argument  \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "MonitorTypes": [
            "MT_QCE"
        ],
        "MonitorTypeInfos": [
            {
                "Id": "1002",
                "Name": "MT_QCE",
                "SortId": 1
            }
        ],
        "RequestId": "d96ec542-6547-4af2-91ac-fee85c1b8b85"
    }
}
```

