**Example 1: 流量示例**

流量示例

Input: 

```
tccli cfw DescribeVpcFwIpStat --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Ip": "192.168.1.1",
                "InstanceId": "ins - a0eksp50",
                "InstanceName": "andy的实例",
                "VpcId": "vpc - a0eksp50",
                "VpcName": "私有网络名称",
                "FlowMax": 11,
                "FlowAvg": 2222,
                "TcRuleStatus": 1,
                "FwInsId": "cfwew - a0eksp50",
                "IpVersion": 1
            }
        ],
        "RequestId": "128c5a96-3656-45a3-968b-14d35529e18e",
        "Total": 0
    }
}
```

