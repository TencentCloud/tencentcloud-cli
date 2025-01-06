**Example 1: 更新函数配置**

更新函数配置

Input: 

```
tccli scf UpdateFunctionConfiguration --cli-unfold-argument  \
    --FunctionName functionName1 \
    --Namespace default \
    --Timeout 100 \
    --VpcConfig.SubnetId subnet-xxxx \
    --VpcConfig.VpcId vpc-xxxxx \
    --MemorySize 512
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

