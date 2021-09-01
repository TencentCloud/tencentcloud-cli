**Example 1: 查询ES集群日志**

查询实例最新的主日志

Input: 

```
tccli es DescribeInstanceLogs --cli-unfold-argument  \
    --InstanceId es-f5mwm28u
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
                "Level": "INFO",
                "Message": "[o.e.p.o.OPackActionFilter] [1547723102001286009] forbidden request: { ID:cdc62072721547678872c0448c1ecaf9, TYP:MainRequest, USR:null, BRS:false, ACT:cluster:monitor/main, OA:10.0.128.43, IDX:, MET:GET, PTH:/, CNT:<OMITTED, LENGTH=0>, HDR:content-length, EFF:0 } Reason: null"
            },
            {
                "Time": "2019-01-22T10:45:35.730+08:00",
                "Ip": "10.0.128.65",
                "Level": "INFO",
                "Message": "[o.e.p.o.OPackActionFilter] [1547723102001286009] forbidden request: { ID:1a8a5b7ea41a485ebdd769586c1dcdf6, TYP:MainRequest, USR:null, BRS:false, ACT:cluster:monitor/main, OA:10.0.128.73, IDX:, MET:GET, PTH:/, CNT:<OMITTED, LENGTH=0>, HDR:content-length, EFF:0 } Reason: null"
            }
        ],
        "RequestId": "783d9290-dc60-4862-9340-10b632605374"
    }
}
```

