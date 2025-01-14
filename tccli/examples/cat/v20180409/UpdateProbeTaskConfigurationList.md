**Example 1: 更新拨测任务配置**



Input: 

```
tccli cat UpdateProbeTaskConfigurationList --cli-unfold-argument  \
    --TaskIds task-xx \
    --Interval 30 \
    --Nodes 10001 \
    --Parameters {"ipType":0,"netIcmpOn":1,"netIcmpActivex":0,"netIcmpTimeout":20,"netIcmpInterval":"0.5","netIcmpNum":4,"netIcmpSize":4,"netIcmpDataCut":1,"netDnsOn":0,"netTracertOn":1,"netTracertTimeout":20,"netTracertNum":0} \
    --Cron * 0-6 * * *
```

Output: 
```
{
    "Response": {
        "RequestId": "720b3231-5a85-4f05-aaab-c9b9596xxxxx"
    }
}
```

