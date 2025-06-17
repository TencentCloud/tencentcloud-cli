**Example 1: 查询指定实例列表的实例属性**



Input: 

```
tccli cvm DescribeInstancesAttributes --cli-unfold-argument  \
    --Attributes UserData \
    --InstanceIds ins-pgklxcq0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "Attributes": {
                    "UserData": "TXlVc2VyRGF0YQo="
                },
                "InstanceId": "ins-pgklxcq0"
            }
        ],
        "RequestId": "bd249418-331b-43c7-b872-3ae94fe84af9"
    }
}
```

