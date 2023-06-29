**Example 1: 示例1**



Input: 

```
tccli keewidb ModifyNetworkConfig --cli-unfold-argument  \
    --InstanceId kee-9clk**** \
    --Operation changeVip
```

Output: 
```
{
    "Response": {
        "RequestId": "929c9b9f-e451-4413-af27-045e4ad8a0d7",
        "Status": true,
        "SubnetId": "subnet-lknn****",
        "Vip": "10.0.16.44",
        "VpcId": "vpc-hqy2****"
    }
}
```

