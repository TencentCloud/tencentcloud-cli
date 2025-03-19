**Example 1: 示例**

示例

Input: 

```
tccli mqtt CreateInstance --cli-unfold-argument  \
    --InstanceType BASIC \
    --Name instance-1 \
    --SkuCode basic_1k \
    --Remark this is remark \
    --VpcList.0.VpcId vpc-9a5wnirv \
    --VpcList.0.SubnetId subnet-0tw6tlfi \
    --IpRules.0.Ip 1.1.1.1 \
    --IpRules.0.Allow True \
    --IpRules.0.Remark remark
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "InstanceId": "mqtt-7pnqmkrx",
        "RequestId": "request-id"
    }
}
```

