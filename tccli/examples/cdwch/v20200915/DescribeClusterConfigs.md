**Example 1: 获取集群配置文件内容**

在xml方式下修改配置文件内容时，获取集群配置文件内容

Input: 

```
tccli cdwch DescribeClusterConfigs --cli-unfold-argument  \
    --InstanceId cdwch-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ClusterConfList": [
            {
                "FilePath": "xx",
                "OriParam": "xx",
                "NeedRestart": 1,
                "FileName": "xx",
                "FileConf": "xx",
                "KeyConf": "xx"
            }
        ]
    }
}
```

