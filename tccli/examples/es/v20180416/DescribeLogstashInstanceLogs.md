**Example 1: 获取Logstash实例日志**



Input: 

```
tccli es DescribeLogstashInstanceLogs --cli-unfold-argument  \
    --InstanceId ls-f5mwm28u
```

Output: 
```
{
    "Response": {
        "TotalCount": 71633,
        "InstanceLogList": [
            {
                "Time": "2019-01-22T10:45:36.220+08:00",
                "Ip": "10.0.128.65",
                "NodeID": "12123141441",
                "Level": "INFO",
                "Message": "[o.e.p.o.OPackActionFilter] [1547723102001286009] forbidden request: { ID:cdcxxxabc, TYP:MainRequest, USR:null, BRS:false, ACT:cluster:monitor/main, OA:10.0.128.43, IDX:, MET:GET, PTH:/, CNT:<OMITTED, LENGTH=0>, HDR:content-length, EFF:0 } Reason: null"
            },
            {
                "Time": "2019-01-22T10:45:35.730+08:00",
                "NodeID": "12123141442",
                "Ip": "10.0.128.65",
                "Level": "INFO",
                "Message": "[o.e.p.o.OPackActionFilter] [1547723102001286009] forbidden request: { ID:1a8axxxabc, TYP:MainRequest, USR:null, BRS:false, ACT:cluster:monitor/main, OA:10.0.128.73, IDX:, MET:GET, PTH:/, CNT:<OMITTED, LENGTH=0>, HDR:content-length, EFF:0 } Reason: null"
            }
        ],
        "RequestId": "783d9290-dc60-4862-9340-10b632605374"
    }
}
```

