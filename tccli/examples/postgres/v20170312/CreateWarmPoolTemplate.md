**Example 1: 创建资源池模版**



Input: 

```
tccli postgres CreateWarmPoolTemplate --cli-unfold-argument  \
    --Name test_my_template \
    --Mode full \
    --InstanceCategory normal \
    --ZoneKey ap-guangzhou-2,ap-guangzhou-3 \
    --Cpu 1 \
    --Memory 2048 \
    --Storage 10 \
    --DBMajorVersion 18 \
    --StorageType PHYSICAL_LOCAL_SSD \
    --VpcId vpc-a27ykb0r \
    --SubnetId subnet-3hekhnki \
    --Target 1 \
    --MinReady 1 \
    --MaxReady 1 \
    --Description 测试模版用例 \
    --SecurityGroupIds sg-bisigzhp \
    --Priority 10 \
    --CallerToken **********************Dq*d7Y****************
```

Output: 
```
{
    "Response": {
        "Name": "test_my_template",
        "RequestId": "3425f798-3158-4785-9dd1-0a1bdc16881b"
    }
}
```

