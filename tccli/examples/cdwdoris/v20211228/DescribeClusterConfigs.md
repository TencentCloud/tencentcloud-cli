**Example 1: 获取集群配置文件内容**

在xml方式下修改配置文件内容时，获取集群配置文件内容

Input: 

```
tccli cdwdoris DescribeClusterConfigs --cli-unfold-argument  \
    --InstanceId cdwch-xxxx
```

Output: 
```
{
    "Response": {
        "ClusterConfList": [
            {
                "NeedRestart": 1,
                "OriParam": "ss=sc",
                "KeyConf": "ss=sc",
                "FileConf": "ss=sc",
                "FileName": "test"
            }
        ],
        "RequestId": "xx-aa"
    }
}
```

