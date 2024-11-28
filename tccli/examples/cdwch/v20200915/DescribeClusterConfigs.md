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
        "ClusterConfList": [
            {
                "FileName": "abc",
                "FileConf": "abc",
                "KeyConf": "abc",
                "OriParam": "abc",
                "NeedRestart": 0,
                "FilePath": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

