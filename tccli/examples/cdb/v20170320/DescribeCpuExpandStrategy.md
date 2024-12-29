**Example 1: 查询实例的弹性扩容配置**

用于查询实例的弹性扩容配置。

Input: 

```
tccli cdb DescribeCpuExpandStrategy --cli-unfold-argument  \
    --InstanceId cdb-sad1dsfa
```

Output: 
```
{
    "Response": {
        "Type": "auto",
        "ExpandCpu": "4",
        "AutoStrategy": "auto",
        "RequestId": "dasdqw13-dasdhd3-123v-1234-v432"
    }
}
```

