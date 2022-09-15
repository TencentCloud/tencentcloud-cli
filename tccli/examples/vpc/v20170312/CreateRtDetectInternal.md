**Example 1: 添加实时探测**



Input: 

```
tccli vpc CreateRtDetectInternal --cli-unfold-argument  \
    --AddRtDetectSet.0.VpcId 1 \
    --AddRtDetectSet.0.Protocol tcp \
    --AddRtDetectSet.0.Ip 10.6.2.3 \
    --AddRtDetectSet.0.Interval 3 \
    --AddRtDetectSet.0.Port 8181 \
    --AddRtDetectSet.0.Sample 0 \
    --AddRtDetectSet.0.Timeout 3 \
    --AddRtDetectSet.0.Type 1 \
    --AddRtDetectSet.0.GroupId 1
```

Output: 
```
{
    "Response": {
        "AddRtDetectResult": [
            {
                "GroupId": 0,
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "Protocol": "tcp",
                "Ip": "10.0.0.2",
                "Interval": 3,
                "Sample": 0,
                "ReturnCode": 1,
                "ReturnMsg": "success",
                "Timeout": 3,
                "Res": [
                    {
                        "Ip": "1.1.1.1",
                        "Delay": 0,
                        "State": 0,
                        "VpcGateway": "1.1.1.1"
                    }
                ],
                "VpcGatewayInstance": [
                    "9.170.232.10"
                ],
                "Port": 80
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

