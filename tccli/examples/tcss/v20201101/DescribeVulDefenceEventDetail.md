**Example 1: 查询漏洞防御事件详情**

查询漏洞防御事件详情

Input: 

```
tccli tcss DescribeVulDefenceEventDetail --cli-unfold-argument  \
    --EventID 0
```

Output: 
```
{
    "Response": {
        "EventDetail": {
            "CVEID": "CVE-2021-44228",
            "City": "",
            "ClusterID": "",
            "ClusterName": "",
            "ContainerID": "5457113fd88a5cc8f88391f7387ad2f1b23c4b9a154f12fc725cfa8b134134",
            "ContainerIsolateOperationSrc": "",
            "ContainerName": "/cve-2021-44228-solr-1",
            "ContainerNetStatus": "",
            "ContainerNetSubStatus": "",
            "ContainerStatus": "",
            "Description": "访问源（IP：）在对容器（ID：5457113fd8...）发起漏洞利用攻击",
            "EventCount": 20,
            "EventID": 30061,
            "EventType": "EVENT_DEFENDED",
            "HostIP": "172.16.51.209",
            "HostName": "harborV2_yancyw",
            "ImageID": "sha256:052794134d434bc2db0775211589beb372412af333a262d16841893418941894",
            "ImageName": "vulhub/solr:8.11.0",
            "JNDIUrl": "",
            "MainClass": "org.eclipse.jetty.start.Main",
            "Namespace": "",
            "NetworkPayload": ": \n",
            "NodeID": "",
            "NodeSubNetCIDR": "",
            "NodeSubNetID": "",
            "NodeSubNetName": "",
            "NodeType": "NORMAL",
            "NodeUniqueID": "",
            "OfficialSolution": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://logging.apache.org/log4j/2.x/security.html",
            "PID": 20545,
            "PocID": "pcmgr-333393",
            "PodIP": "",
            "PodName": "",
            "PublicIP": "139.199.178.111",
            "QUUID": "380add75-bb06-4cc4-84c5-cf806d102fba",
            "RaspDetail": [
                {
                    "Name": "jndiurl",
                    "Value": "ldap://1.8.0_102.example.com"
                }
            ],
            "ServerAccount": "",
            "ServerArg": "",
            "ServerExe": "",
            "ServerPort": "",
            "SourceIP": "",
            "SourcePort": [
                "-"
            ],
            "StackTrace": "org.apache.logging.log4j.core.lookup.JndiLookup.lookup\norg.apache.logging.log4j.core.lookup.Interpolator.lookup\norg.apache.logging.log4j.core.lookup.StrSubstitutor.resolveVariable\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.substitute\norg.apache.logging.log4j.core.lookup.StrSubstitutor.replace\norg.apache.logging.log4j.core.pattern.MessagePatternConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\norg.apache.logging.log4j.core.pattern.MaxLengthConverter.format\norg.apache.logging.log4j.core.pattern.PatternFormatter.format\n",
            "Status": "EVENT_DEFENDED",
            "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
            "WorkloadType": ""
        },
        "RequestId": "2f944254-e774-4f19-ac09-c9c1bdf311f6"
    }
}
```

