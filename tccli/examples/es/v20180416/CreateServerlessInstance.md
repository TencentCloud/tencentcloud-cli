**Example 1: 创建Serverless实例**

创建Serverless实例

Input: 

```
tccli es CreateServerlessInstance --cli-unfold-argument  \
    --SubnetId xx \
    --IndexMetaJson xx \
    --VpcId xx \
    --IndexName xx \
    --Zone xx \
    --SpaceId xx
```

Output: 
```
{
    "Response": {
        "InstanceId": "xx",
        "RequestId": "xx",
        "DealName": "xx"
    }
}
```

