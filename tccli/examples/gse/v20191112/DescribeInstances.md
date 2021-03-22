**Example 1: 查询实例列表**



Input: 

```
tccli gse DescribeInstances --cli-unfold-argument  \
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
                "CreateTime": "2020-04-09T11:30:03Z",
                "DnsName": "",
                "FleetId": "fleet-qp3g3caa-dglymksw",
                "InstanceId": "ins-1d6i1mzp",
                "IpAddress": "1.1.1.1",
                "OperatingSystem": "CentOS7.16",
                "Status": "RUNNING",
                "Type": "S5.SMALL2"
            },
            {
                "CreateTime": "2020-04-09T11:20:20Z",
                "DnsName": "",
                "FleetId": "fleet-qp3g3caa-ckyp9do4",
                "InstanceId": "ins-gsua7xs9",
                "IpAddress": "1.1.1.2",
                "OperatingSystem": "CentOS7.16",
                "Status": "RUNNING",
                "Type": "S5.SMALL2"
            }
        ],
        "RequestId": "e8ab591f-9a69-466d-a27b-a587556856bc",
        "TotalCount": 2
    }
}
```

