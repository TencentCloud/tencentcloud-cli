**Example 1: 示例1**



Input: 

```
tccli cat CreateProbeTasks --cli-unfold-argument  \
    --BatchTasks.0.TargetAddress http://www.baidu.com \
    --BatchTasks.0.Name CDN验证21 \
    --Parameters {"ipType":0,"grabBag":0,"netIcmpOn":1,"netIcmpActivex":0,"netIcmpTimeout":20,"netIcmpInterval":0.5,"netIcmpNum":20,"netIcmpSize":32,"netIcmpDataCut":1,"netDnsOn":1,"netDnsTimeout":5,"netDnsQuerymethod":1,"netDnsNs":"","netDigOn":1,"netDnsServer":2,"netTracertOn":1,"netTracertTimeout":60,"netTracertNum":30,"whiteList":"","blackList":"","netIcmpActivexStr":""} \
    --TaskCategory 1 \
    --Interval 5 \
    --TaskType 5 \
    --Nodes 12136
```

Output: 
```
{
    "Response": {
        "RequestId": "0c4977a0-5b9f-469b-84d4-5d6a609e93a3",
        "TaskIDs": [
            "task-h4bcnook"
        ]
    }
}
```

**Example 2: 批量创建拨测任务**



Input: 

```
tccli cat CreateProbeTasks --cli-unfold-argument  \
    --BatchTasks.0.Name probe \
    --BatchTasks.0.TargetAddress http://www.baidu.com \
    --Parameters {"ipType":0,"grabBag":0,"netIcmpOn":1,"netIcmpActivex":0,"netIcmpTimeout":20,"netIcmpInterval":0.5,"netIcmpNum":20,"netIcmpSize":32,"netIcmpDataCut":1,"netDnsOn":1,"netDnsTimeout":5,"netDnsQuerymethod":1,"netDnsNs":"","netDigOn":1,"netDnsServer":2,"netTracertOn":1,"netTracertTimeout":60,"netTracertNum":30,"whiteList":"","blackList":"","netIcmpActivexStr":""} \
    --Interval 30 \
    --TaskCategory 1 \
    --TaskType 5 \
    --Nodes 10001 \
    --Cron * 0-6 * * * \
    --Tag.0.TagKey 运营部门 \
    --Tag.0.TagValue 产一
```

Output: 
```
{
    "Response": {
        "TaskIDs": [
            "task-abc"
        ],
        "RequestId": "720b3231-5a85-4f05-aaab-c9b9596xxxxx"
    }
}
```

