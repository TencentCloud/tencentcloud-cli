**Example 1: 示例**



Input: 

```
tccli es CreateServerlessSpaceV2 --cli-unfold-argument  \
    --SpaceName abc \
    --VpcInfo.0.VpcId abc \
    --VpcInfo.0.SubnetId abc \
    --VpcInfo.0.VpcUid 1 \
    --VpcInfo.0.SubnetUid 1 \
    --VpcInfo.0.AvailableIpAddressCount 0 \
    --Zone abc \
    --KibanaWhiteIpList abc \
    --ZoneId 1
```

Output: 
```
{
    "Response": {
        "SpaceId": "abc",
        "RequestId": "abc"
    }
}
```

