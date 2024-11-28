**Example 1: 创建专享实例**

创建专享实例

Input: 

```
tccli apigateway CreateExclusiveInstances --cli-unfold-argument  \
    --Zones ap-beijing-5 ap-beijing-6 \
    --InstanceName test \
    --InstanceDescription test \
    --InstanceType basic \
    --NetworkConfig.InternetMaxBandwidthOut 5000 \
    --VpcConfig.UniqVpcId vpc-6bjypxxxx \
    --VpcConfig.UniqSubnetId subnet-rd2xxxx \
    --PayMode POSTPAID
```

Output: 
```
{
    "Response": {
        "RequestId": "a6dcc75c-d10f-4b37-bff8-a5cc7be6fa7a",
        "Result": "instance-lxxxxxxx"
    }
}
```

