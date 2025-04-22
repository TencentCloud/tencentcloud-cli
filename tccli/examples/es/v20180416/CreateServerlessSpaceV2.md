**Example 1: 示例**



Input: 

```
tccli es CreateServerlessSpaceV2 --cli-unfold-argument  \
    --SpaceName spaceName \
    --VpcInfo.0.VpcId vpc-feafeaf \
    --VpcInfo.0.SubnetId subnet-feafaffg \
    --VpcInfo.0.VpcUid 1 \
    --VpcInfo.0.SubnetUid 1 \
    --VpcInfo.0.AvailableIpAddressCount 0 \
    --Zone ap-guangzhou-1 \
    --KibanaWhiteIpList 127.0.0.1 \
    --ZoneId 100001
```

Output: 
```
{
    "Response": {
        "SpaceId": "space-feafaefgg",
        "RequestId": "40f4f780-9969-42f9-8bd9-ccf0d1f2591a"
    }
}
```

