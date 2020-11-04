**Example 1: 服务器舰队安全组信息查询**

服务器舰队安全组信息查询

Input: 

```
tccli gse DescribeFleetPortSettings --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-nkeekxw6
```

Output: 
```
{
    "Response": {
        "InboundPermissions": [
            {
                "FromPort": 1900,
                "IpRange": "0.0.0.0/0",
                "Protocol": "TCP",
                "ToPort": 2900
            }
        ],
        "RequestId": "16f29370-828e-4acc-a836-9a542abfb650"
    }
}
```

