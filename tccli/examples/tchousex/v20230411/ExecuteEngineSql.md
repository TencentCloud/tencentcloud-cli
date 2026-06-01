**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex ExecuteEngineSql --cli-unfold-argument  \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993 \
    --SQL select * from test.t1
```

Output: 
```
{
    "Response": {
        "RequestId": "77f31571-02a5-44c8-ad90-928c9031f8ee"
    }
}
```

