**Example 1: 查询实例及其扩展信息**



Input: 

```
tccli gse DescribeInstancesExtend --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-ay03mhdm \
    --IpAddress 1.1.1.1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "ActiveProcessCnt": 1,
                "GameSessionCnt": 0,
                "HealthyProcessCnt": 1,
                "Instance": {
                    "CreateTime": "2020-02-26T03:31:17Z",
                    "DnsName": "",
                    "FleetId": "fleet-qp3g3caa-19tzbzao",
                    "InstanceId": "ins-242yfav7",
                    "IpAddress": "129.211.106.166",
                    "OperatingSystem": "CentOS7.16",
                    "Status": "RUNNING",
                    "Type": "S5.SMALL2"
                },
                "MaxGameSessionCnt": 0,
                "MaxPlayerSessionCnt": 0,
                "PlayerSessionCnt": 0,
                "State": "Active"
            }
        ],
        "RequestId": "d47e19b5-12b7-43e9-b25f-a48344efb199",
        "TotalCount": 1
    }
}
```

