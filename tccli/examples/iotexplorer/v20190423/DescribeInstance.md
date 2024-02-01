**Example 1: 实例详情**



Input: 

```
tccli iotexplorer DescribeInstance --cli-unfold-argument  \
    --ProjectId prj-1aoioii9 \
    --InstanceId ins-BoSq3gRJ27 \
    --ProductId -1
```

Output: 
```
{
    "Response": {
        "Data": {
            "InstanceId": "ins-BoSq3gRJ27",
            "InstanceType": 0,
            "Region": "ap-guangzhou",
            "ZoneId": "",
            "TotalDeviceNum": 1000,
            "ProjectNum": 0,
            "ProductNum": 0,
            "UsedDeviceNum": 15,
            "CreateTime": "2021-05-26T10:57:52+08:00",
            "UpdateTime": "2021-07-20T14:52:16+08:00",
            "ExpireTime": "0001-01-01T00:00:00Z",
            "TotalDevice": 15,
            "ActivateDevice": 0,
            "Description": "",
            "Status": 0
        },
        "RequestId": "8bbbaa15-9918-4fd9-a70c-dbb47dwac0ca"
    }
}
```

