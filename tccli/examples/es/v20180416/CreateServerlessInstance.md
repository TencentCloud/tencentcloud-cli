**Example 1: 创建serverless实例**

创建serverless实例

Input: 

```
tccli es CreateServerlessInstance --cli-unfold-argument  \
    --Zone abc \
    --VpcId abc \
    --SubnetId abc \
    --IndexName abc \
    --IndexMetaJson {} \
    --SpaceId abc \
    --Username abc \
    --Password abc
```

Output: 
```
{
    "Response": {
        "InstanceId": "abc",
        "DealName": "abc",
        "RequestId": "abc"
    }
}
```

