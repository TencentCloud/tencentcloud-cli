**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeDatabaseByName --cli-unfold-argument  \
    --Name test \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993
```

Output: 
```
{
    "Response": {
        "Description": "",
        "ExtParameters": null,
        "Name": "test",
        "RequestId": "f57ab800-96ec-4ba5-87eb-ca15720de186"
    }
}
```

