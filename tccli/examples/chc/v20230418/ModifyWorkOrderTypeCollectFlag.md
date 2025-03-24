**Example 1: 修改网络通用服务的收藏标识**



Input: 

```
tccli chc ModifyWorkOrderTypeCollectFlag --cli-unfold-argument  \
    --WorkOrderType netDeviceCommon
```

Output: 
```
{
    "Response": {
        "CurrentCollectFlag": true,
        "RequestId": "14ec2fbf-8b7d-4b55-ba69-207d7ca6c15e"
    }
}
```

