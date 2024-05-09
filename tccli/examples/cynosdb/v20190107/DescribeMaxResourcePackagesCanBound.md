**Example 1: 查询cynos集群最大可绑定资源包个数**

查询cynos集群最大可绑定资源包个数

Input: 

```
tccli cynosdb DescribeMaxResourcePackagesCanBound --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MaxResourcePackagesCanBound": 10,
        "RequestId": "abc"
    }
}
```

