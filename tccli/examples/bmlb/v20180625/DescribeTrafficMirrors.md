**Example 1: 获取流量镜像实例的列表信息**



Input: 

```
tccli bmlb DescribeTrafficMirrors --cli-unfold-argument  \
    --TrafficMirrorIds bmtm-lmep0eit \
    --Aliases test \
    --VpcIds vpc-muinpf9p
```

Output: 
```
{
    "Response": {
        "TrafficMirrorSet": [
            {
                "TrafficMirrorId": "bmtm-lmep0eit",
                "Alias": "test",
                "VpcId": "vpc-muinpf9p",
                "HealthSwitch": 0,
                "HealthNum": 3,
                "UnhealthNum": 3,
                "IntervalTime": 5,
                "HttpCheckDomain": "",
                "HttpCheckPath": "",
                "HttpCodes": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "d2796e3b-cc73-424e-97d1-31d26fd0d1d7"
    }
}
```

