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
                "FileName": "hosts",
                "FileConf": "",
                "KeyConf": "",
                "OriParam": "",
                "NeedRestart": 0,
                "FilePath": "/etc"
            }
        ],
        "RequestId": "e5733734-4226-4949-b692-333a6301399e"
    }
}
```

