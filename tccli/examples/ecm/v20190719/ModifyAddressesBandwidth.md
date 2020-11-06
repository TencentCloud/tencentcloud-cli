**Example 1: 调整EIP带宽**



Input: 

```
tccli ecm ModifyAddressesBandwidth --cli-unfold-argument  \
    --InternetMaxBandwidthOut 1000 \
    --AddressIds eip-11112222 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TaskId": "123",
        "RequestId": "24cfceab-3492-482c-b86f-27f598b1b044"
    }
}
```

