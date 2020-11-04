**Example 1: 查询实例流量包详情**



Input: 

```
tccli lighthouse DescribeInstancesTrafficPackages --cli-unfold-argument  \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceTrafficPackageSet": [
            {
                "InstanceId": "lhins-7h98ep3z",
                "TrafficPackageSet": [
                    {
                        "TrafficPackageId": "lhtfp-o1wtyyvx",
                        "TrafficUsed": 5905577,
                        "TrafficPackageTotal": 536870912000,
                        "TrafficPackageRemaining": 536865006423,
                        "TrafficOverflow": 0,
                        "StartTime": "2020-06-28T08:15:18Z",
                        "EndTime": "2020-07-28T08:15:17Z",
                        "Deadline": "2020-07-28T08:15:18Z",
                        "Status": "NETWORK_NORMAL"
                    }
                ]
            },
            {
                "InstanceId": "lhins-abtdx7eb",
                "TrafficPackageSet": [
                    {
                        "TrafficPackageId": "lhtfp-4noj8p75",
                        "TrafficUsed": 3435972,
                        "TrafficPackageTotal": 536870912000,
                        "TrafficPackageRemaining": 536867476028,
                        "TrafficOverflow": 0,
                        "StartTime": "2020-06-28T08:08:57Z",
                        "EndTime": "2020-07-28T08:08:56Z",
                        "Deadline": "2020-07-28T08:08:57Z",
                        "Status": "NETWORK_NORMAL"
                    }
                ]
            }
        ],
        "RequestId": "7839b8ee-f5a4-4a67-b1ab-15fb35b1e2fe"
    }
}
```

