**Example 1: 查询漏洞防御事件详情**

查询漏洞防御事件详情

Input: 

```
tccli tcss DescribeVulDefenceEventDetail --cli-unfold-argument  \
    --EventID 1002
```

Output: 
```
{
    "Response": {
        "EventDetail": {
            "CVEID": "CVE-2021-44228",
            "City": "Beijing",
            "ClusterID": "cls-dfw3e***",
            "ClusterName": "clsfoo***",
            "ContainerID": "5457113fd88a5cc8f88391f7387ad2f1b23c4b9a154f12fc725cfa8b134134",
            "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
            "ContainerName": "/cve-2021-44228-solr-1",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "ContainerStatus": "RUNNING",
            "Description": "访问源（IP：）在对容器（ID：5457113fd8...）发起漏洞利用攻击",
            "EventCount": 20,
            "EventID": 30061,
            "EventType": "EVENT_DEFENDED",
            "HostIP": "172.16.51.209",
            "HostName": "harborV2_yancyw",
            "ImageID": "sha256:052794134d434bc2db0775211589beb372412af333a262d16841893418941894",
            "ImageName": "vulhub/solr:8.11.0",
            "JNDIUrl": "http://10.0.0.1",
            "MainClass": "org.eclipse.jetty.start.Main",
            "Namespace": "tcss",
            "NetworkPayload": ": \n",
            "NodeID": "mix-GOmf****",
            "NodeSubNetCIDR": "10.0.200.0/24",
            "NodeSubNetID": "subnet-5gu2***",
            "NodeSubNetName": "subnet***",
            "NodeType": "NORMAL",
            "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
            "OfficialSolution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://logging.apache.org/log4j/2.x/security.html",
            "PID": 20545,
            "PocID": "pcmgr-333393",
            "PodIP": "10.0.1.92",
            "PodName": "agent-test-2zrp7",
            "PublicIP": "127.2.3.4",
            "QUUID": "380add75-bb06-4cc4-84c5-cf806d102fba",
            "RaspDetail": [
                {
                    "Name": "jndiurl",
                    "Value": "ldap://1.8.0_102.example.com"
                }
            ],
            "ServerAccount": "server account",
            "ServerArg": "server avg",
            "ServerExe": "server exe",
            "ServerPort": "3306",
            "SourceIP": "10.0.1.2",
            "SourcePort": [
                "3306"
            ],
            "StackTrace": "org.apache.logging.log4j.core.lookup.JndiLookup.lookup\norg.apache.logging.log4j.core.lookup.Interpolator.lookup\norg.apache.logging.log4j.core.lookup.StrSubstitutor.resolveVariable\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.replace\norg.apache.logging.log4j.core.pattern.MessagePatternConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\norg.apache.logging.log4j.core.pattern.MaxLengthConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\n",
            "Status": "EVENT_DEFENDED",
            "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
            "WorkloadType": "DaemonSet"
        },
        "RequestId": "2f944254-e774-4f19-ac09-c9c1bdf311f6"
    }
}
```

